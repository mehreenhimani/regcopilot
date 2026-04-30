# RegCopilot — AI Copilot for EU Regulatory Compliance

An AI-powered RAG copilot for compliance officers. Ask questions about EU AI Act, DORA, AMLD6, and GDPR — get citation-grounded answers in seconds.

## Live Demo

- App: https://regcopilot.lovable.app
- Video: https://youtu.be/7b0qE0jCns0

## Tech Stack

- Claude API (claude-sonnet-4-6) — LLM
- Supabase pgvector — vector database
- Lovable — UI + Edge Functions
- Python — chunking + ingestion pipeline

## Architecture

- 641 regulation chunks indexed across 4 EU regulations
- Vector similarity search retrieves top 5 relevant chunks
- Claude generates grounded answers from retrieved context
- Full audit trail logged per query

## Eval Results (v1)

- Overall: 82% (41/50) on 10 golden questions
- GDPR: 5/5 perfect
- DORA: 4.3/5
- EU AI Act: 3.5/5
- AMLD6: 3/5

## V2 Roadmap

- Hybrid search (BM25 + vector)
- Expanded AMLD6 corpus
- Citation display fix
- Auth + role-based access

## Author

Mehreen Himani — Senior AI Product Manager
GitHub: [@mehreenhimani](https://github.com/mehreenhimani)
