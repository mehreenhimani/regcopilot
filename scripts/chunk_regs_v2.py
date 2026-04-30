#!/usr/bin/env python3
"""
Chunk EU regulation PDFs with page-number tracking.

Same chunker as v1 but each chunk records the PDF page it starts on, so we can
emit Edge-Function-ready records {regulation_id, article_reference, page_number, content}
plus the legacy {regulation, article, chapter, text} fields for traceability.

Outputs:
  - ~/Portfolio/RegCopilot/chunks/document_chunks.json     (canonical, with page_number)
  - ~/Portfolio/RegCopilot/chunks/ingest_payload.json      (grouped by regulation_id, ready to POST)
"""
import json
import re
import sys
from pathlib import Path
from collections import defaultdict

import pdfplumber

REG_DIR = Path("/Users/mehreenhimani/Portfolio/RegCopilot/regulations")
OUT_DIR = Path("/Users/mehreenhimani/Portfolio/RegCopilot/chunks")

# Filename -> (display_name, regulation_id slug)
REGULATIONS = {
    "gdpr.pdf":      ("GDPR",       "gdpr"),
    "dora.pdf":      ("DORA",       "dora"),
    "eu_ai_act.pdf": ("EU AI Act",  "eu_ai_act"),
    "amld6.pdf":     ("AMLD6",      "amld6"),
}

ARTICLE_RE      = re.compile(r"^\s*Article\s+(\d+[a-z]?)\s*$", re.IGNORECASE)
CHAPTER_ROMAN_RE = re.compile(r"^\s*CHAPTER\s+([IVXLCDM]+)\s*$")
CHAPTER_NUM_RE   = re.compile(r"^\s*Chapter\s+(\d+)\s*$")

NOISE_RES = [
    re.compile(r"^\s*EN\s*$"),
    re.compile(r"^\s*Official Journal of the European Union\s*$", re.I),
    re.compile(r"^\s*L\s+\d+/\d+\s*$"),
    re.compile(r"^\s*OJ L.*\d{4}\s*$"),
    re.compile(r"^\s*\d{1,2}\.\d{1,2}\.\d{4}\s*$"),
    re.compile(r"^\s*ELI:.*$"),
]

def is_noise(line):
    return any(r.match(line) for r in NOISE_RES)

def extract_lines_with_pages(pdf_path):
    """Yield (line_text, page_number) tuples in document order."""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            txt = page.extract_text() or ""
            for raw in txt.splitlines():
                line = raw.rstrip()
                if not line.strip() or is_noise(line):
                    continue
                yield line, page.page_number  # 1-indexed

def walk_sections(lines_pages):
    """Group line/page pairs into sections keyed by (chapter, article)."""
    current_chapter = None
    current_article = "Preamble"
    buf = []        # list of (line, page)
    sections = []

    def flush():
        if buf:
            sections.append({
                "chapter": current_chapter,
                "article": current_article,
                "lines": list(buf),
            })

    for line, page in lines_pages:
        if CHAPTER_ROMAN_RE.match(line):
            flush(); buf = []
            current_chapter = f"Chapter {CHAPTER_ROMAN_RE.match(line).group(1)}"
            continue
        if CHAPTER_NUM_RE.match(line):
            flush(); buf = []
            current_chapter = f"Chapter {CHAPTER_NUM_RE.match(line).group(1)}"
            continue
        if ARTICLE_RE.match(line):
            flush(); buf = []
            current_article = f"Article {ARTICLE_RE.match(line).group(1)}"
            continue
        buf.append((line, page))

    flush()
    return [s for s in sections if s["lines"]]

def chunk_section(section, size=500, overlap=50):
    """
    Slide a 500-word window over the section's text. Each chunk also records the
    PDF page where its first word came from (page_number = page of first token).
    """
    # Build a flat list of (word, page) tokens
    tokens = []
    for line, page in section["lines"]:
        for w in line.split():
            tokens.append((w, page))
    if not tokens:
        return []

    if len(tokens) <= size:
        text = " ".join(w for w, _ in tokens)
        return [{"text": text, "page_number": tokens[0][1]}]

    step = size - overlap
    chunks = []
    i = 0
    while i < len(tokens):
        window = tokens[i:i+size]
        if not window:
            break
        chunks.append({
            "text": " ".join(w for w, _ in window),
            "page_number": window[0][1],
        })
        if i + size >= len(tokens):
            break
        i += step
    return chunks

def article_reference(article, chapter):
    """Compose a citation string. Drop chapter when null."""
    if not chapter:
        return article            # "Preamble" or "Article 1"
    return f"{chapter} · {article}"  # "Chapter III · Article 22"

def main():
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    canonical_chunks = []
    payload_groups = defaultdict(list)  # regulation_id -> list of {article_reference, page_number, content}
    summary = {}

    for fname, (display, reg_id) in REGULATIONS.items():
        path = REG_DIR / fname
        if not path.exists():
            print(f"WARN: missing {path}", file=sys.stderr); continue

        print(f"Processing {fname} ({display}, regulation_id={reg_id}) ...", flush=True)
        sections = walk_sections(list(extract_lines_with_pages(path)))
        n_chunks = 0
        for sec in sections:
            for ch in chunk_section(sec, 500, 50):
                # Canonical record (kept on disk for downstream uses)
                canonical_chunks.append({
                    "regulation": display,
                    "regulation_id": reg_id,
                    "article": sec["article"],
                    "chapter": sec["chapter"],
                    "page_number": ch["page_number"],
                    "text": ch["text"],
                })
                # Edge Function payload
                payload_groups[reg_id].append({
                    "article_reference": article_reference(sec["article"], sec["chapter"]),
                    "page_number": ch["page_number"],
                    "content": ch["text"],
                })
                n_chunks += 1
        summary[display] = {"sections": len(sections), "chunks": n_chunks}
        print(f"  -> {len(sections)} sections, {n_chunks} chunks", flush=True)

    # Write canonical
    canonical_path = OUT_DIR / "document_chunks.json"
    canonical_path.write_text(json.dumps(canonical_chunks, ensure_ascii=False, indent=2))

    # Write Edge-Function-ready payload (one object per regulation_id, batched server-side)
    ingest_path = OUT_DIR / "ingest_payload.json"
    payload = [{"regulation_id": rid, "chunks": chs} for rid, chs in payload_groups.items()]
    ingest_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2))

    print(f"\nCanonical: {canonical_path} ({canonical_path.stat().st_size/1024:.1f} KB)")
    print(f"Ingest payload: {ingest_path} ({ingest_path.stat().st_size/1024:.1f} KB)")
    print(f"Total chunks: {len(canonical_chunks)}")
    print("\nPer-regulation:")
    for d, s in summary.items():
        print(f"  {d:12s}  {s['chunks']} chunks (from {s['sections']} sections)")

if __name__ == "__main__":
    main()
