#!/usr/bin/env python3
"""
Chunk EU regulation PDFs into ~500-word chunks (50-word overlap) with
per-chunk metadata: regulation, article, chapter.

Output: ~/Portfolio/RegCopilot/chunks/document_chunks.json
"""
import json
import re
import sys
from pathlib import Path

import pdfplumber

REG_DIR = Path("/sessions/zealous-exciting-wright/mnt/RegCopilot/regulations")
OUT_PATH = Path("/sessions/zealous-exciting-wright/mnt/RegCopilot/chunks/document_chunks.json")

# Map filename -> regulation display name
REGULATIONS = {
    "gdpr.pdf": "GDPR",
    "dora.pdf": "DORA",
    "eu_ai_act.pdf": "EU AI Act",
    "amld6.pdf": "AMLD6",
}

# --- Heading detection -------------------------------------------------------
# Line is just "Article N" (possibly with an 'a' suffix), optionally followed
# by spaces. We treat that as a heading.  Pattern is anchored to a full line.
ARTICLE_RE = re.compile(r"^\s*Article\s+(\d+[a-z]?)\s*$", re.IGNORECASE)

# Chapter: "CHAPTER I", "CHAPTER II", etc. — Roman numerals in caps, line on
# its own. Some regs also use "Chapter 1" etc., so be a little forgiving.
CHAPTER_ROMAN_RE = re.compile(r"^\s*CHAPTER\s+([IVXLCDM]+)\s*$")
CHAPTER_NUM_RE = re.compile(r"^\s*Chapter\s+(\d+)\s*$")

# Lines that are pure noise on EUR-Lex layouts — filter so they don't pollute chunks
NOISE_RES = [
    re.compile(r"^\s*EN\s*$"),                                          # language code
    re.compile(r"^\s*Official Journal of the European Union\s*$", re.I),
    re.compile(r"^\s*L\s+\d+/\d+\s*$"),                                  # page refs like "L 119/1"
    re.compile(r"^\s*OJ L.*\d{4}\s*$"),                                  # OJ citation header
    re.compile(r"^\s*\d{1,2}\.\d{1,2}\.\d{4}\s*$"),                      # date stamp dd.mm.yyyy
    re.compile(r"^\s*ELI:.*$"),                                          # ELI URI footer
]

def is_noise(line: str) -> bool:
    return any(r.match(line) for r in NOISE_RES)

# --- Extraction --------------------------------------------------------------
def extract_lines(pdf_path: Path):
    """Yield non-noise text lines from the PDF, in order."""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            txt = page.extract_text() or ""
            for raw in txt.splitlines():
                line = raw.rstrip()
                if not line.strip():
                    continue
                if is_noise(line):
                    continue
                yield line

# --- Section walker ----------------------------------------------------------
def walk_sections(lines):
    """
    Group lines into sections keyed by (chapter, article).

    Returns a list of dicts: {"chapter": str|None, "article": str, "text": str}
    in document order. Article 'Preamble' covers everything before Article 1.
    """
    current_chapter = None
    current_article = "Preamble"
    buf = []
    sections = []

    def flush():
        if buf:
            sections.append({
                "chapter": current_chapter,
                "article": current_article,
                "text": "\n".join(buf).strip(),
            })

    for line in lines:
        m_art = ARTICLE_RE.match(line)
        m_ch_r = CHAPTER_ROMAN_RE.match(line)
        m_ch_n = CHAPTER_NUM_RE.match(line)

        if m_ch_r:
            flush()
            buf = []
            current_chapter = f"Chapter {m_ch_r.group(1)}"
            continue
        if m_ch_n:
            flush()
            buf = []
            current_chapter = f"Chapter {m_ch_n.group(1)}"
            continue
        if m_art:
            flush()
            buf = []
            current_article = f"Article {m_art.group(1)}"
            continue

        buf.append(line)

    flush()
    # Drop any empty-text sections
    return [s for s in sections if s["text"]]

# --- Chunking ----------------------------------------------------------------
def chunk_words(text: str, size: int = 500, overlap: int = 50):
    """Sliding-window chunker on whitespace-tokenized words."""
    words = text.split()
    if not words:
        return []
    if len(words) <= size:
        return [" ".join(words)]
    step = size - overlap
    chunks = []
    i = 0
    while i < len(words):
        window = words[i : i + size]
        if not window:
            break
        chunks.append(" ".join(window))
        if i + size >= len(words):
            break
        i += step
    return chunks

# --- Main --------------------------------------------------------------------
def main():
    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    all_chunks = []
    summary = {}

    for fname, reg_name in REGULATIONS.items():
        path = REG_DIR / fname
        if not path.exists():
            print(f"WARN: missing {path}", file=sys.stderr)
            continue
        print(f"Processing {fname} ({reg_name}) ...", flush=True)
        lines = list(extract_lines(path))
        sections = walk_sections(lines)
        n_chunks_for_reg = 0
        for sec in sections:
            for chunk_text in chunk_words(sec["text"], 500, 50):
                all_chunks.append({
                    "regulation": reg_name,
                    "article": sec["article"],
                    "chapter": sec["chapter"],
                    "text": chunk_text,
                })
                n_chunks_for_reg += 1
        summary[reg_name] = {
            "lines": len(lines),
            "sections": len(sections),
            "chunks": n_chunks_for_reg,
        }
        print(f"  -> {len(lines)} lines, {len(sections)} sections, {n_chunks_for_reg} chunks", flush=True)

    OUT_PATH.write_text(json.dumps(all_chunks, ensure_ascii=False, indent=2))
    print(f"\nWrote {len(all_chunks)} chunks to {OUT_PATH}")
    print(f"File size: {OUT_PATH.stat().st_size / 1024:.1f} KB")
    print("\nSummary:")
    for reg, s in summary.items():
        print(f"  {reg}: {s['chunks']} chunks (from {s['sections']} sections, {s['lines']} lines)")

if __name__ == "__main__":
    main()
