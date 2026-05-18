# FinSight AI 🔍

> Autonomous financial research agent — LangGraph · Corrective RAG · FastAPI · React

[![FastAPI](https://img.shields.io/badge/FastAPI-0.115-009688?logo=fastapi)](https://fastapi.tiangolo.com)
[![LangGraph](https://img.shields.io/badge/LangGraph-0.2-blue)](https://langchain-ai.github.io/langgraph/)
[![React](https://img.shields.io/badge/React-18-61DAFB?logo=react)](https://react.dev)
[![Python](https://img.shields.io/badge/Python-3.11+-3776AB?logo=python)](https://python.org)

**Status:** 🚧 In development — Day 1 scaffold

---

## What it does

Give FinSight a stock ticker (e.g. `AAPL`) and it autonomously:

1. **Plans** research tasks via an Orchestrator agent
2. **Retrieves** evidence using Corrective RAG (HyDE + MMR + cross-encoder grading)
3. **Analyses** financials via tool calls (SEC EDGAR MCP, yfinance, Brave search, Python REPL)
4. **Critiques** its own output for hallucinations and risk flags
5. **Streams** everything live to a dark-terminal React dashboard

---

## Tech stack

| Layer | Technology |
|---|---|
| Frontend | React 18 + Vite + Tailwind CSS + Zustand |
| Backend | FastAPI + Uvicorn (async) + Pydantic v2 |
| AI | LangGraph StateGraph + LangChain LCEL + Claude Sonnet |
| RAG | ChromaDB + HyDE + MMR + Cross-encoder + Corrective RAG |
| Database | SQLite via aiosqlite + LangGraph AsyncSqliteSaver |
| Observability | LangSmith (full trace per run) |
| Tools / MCP | EDGAR MCP · yfinance · Brave · Python REPL |
| Agentic coding | Claude Code (SPEC.md · /commands · skills · hooks) |
| Deploy | Vercel (frontend) + Render (backend) |

---

## Quick start (local dev)

```bash
# 1. Clone
git clone https://github.com/<you>/finsight.git
cd finsight

# 2. Environment
cp .env.example .env
# Fill in ANTHROPIC_API_KEY and LANGCHAIN_API_KEY at minimum

# 3. Install
make install

# 4. Initialise database
make db-init

# 5. Run (two terminals)
make dev-backend    # FastAPI on :8000
make dev-frontend   # React on :5173
```

Open http://localhost:5173 — the dashboard will connect to FastAPI automatically.

---

## Project structure

```
finsight/
├── backend/          FastAPI app, routers, schemas, services
├── agents/           LangGraph StateGraph, nodes, RAG pipeline, tools
├── frontend/         React + Vite dashboard
├── claude-code/      SPEC.md, /commands, skills, hooks
├── tests/            pytest + vitest suites
├── Makefile          All dev commands
└── render.yaml       Render deployment config
```

---

## Skills demonstrated

| Skill | Component |
|---|---|
| LangGraph · Nodes · Edges | Orchestrator StateGraph with conditional CRAG edge |
| Corrective RAG | Grader node, fallback web search, re-query loop |
| Advanced RAG | HyDE query expansion, MMR, cross-encoder re-ranking |
| FastAPI | REST + WebSocket backend, Pydantic v2, async/await |
| Observability | LangSmith tracer → live WebSocket trace log in UI |
| Persistence · Memory | AsyncSqliteSaver checkpointer, multi-turn sessions |
| Tool calling + MCP | EDGAR, yfinance, Brave, Python REPL |
| Agentic AI (Claude Code) | SPEC.md, /commands, skills, pre/post hooks |

---

*Built as an AI engineering portfolio project — 8-week roadmap.*
