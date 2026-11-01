# Curriculum QA Agents

Two LlamaIndex agents that **generate** classroom MCQs and then **validate** them before they ship.

## Pipeline

1. **Agent 1 — Generate** (`ag1.py`): curriculum teacher persona creates N questions with options + answers for a chapter/subtopic.
2. **Agent 2 — Validate** (`ag2.py`): second pass checks structure and teaching quality.
3. **Orchestrator** (`main.py`): wires the hand-off for a single run.

## Why hiring teams care

Shows multi-agent separation of concerns (author vs critic), not a single prompt dumping JSON.

## Stack

Python · LlamaIndex · OpenAI

## Quick start

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install llama-index openai
export OPENAI_API_KEY=...
python main.py
```

## Related

- `subject-checklist-validator` — checklist-driven scoring for the same domain
