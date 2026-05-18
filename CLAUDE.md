# FinSight AI — Claude Code Guide

Autonomous financial research agent: give it a ticker, it plans, retrieves, analyses, critiques, and streams results live.

---

## What we are building

FinSight takes a stock ticker (e.g. `AAPL`) and runs a multi-agent pipeline:

1. **Orchestrator** — plans research tasks via LangGraph StateGraph
2. **Corrective RAG** — HyDE query expansion → ChromaDB retrieval → MMR + cross-encoder grading → fallback web search
3. **Tool agents** — SEC EDGAR MCP, yfinance, Brave search, Python REPL
4. **Critic** — checks output for hallucinations and risk flags
5. **Dashboard** — streams everything live over WebSocket to a React terminal UI

---

## Tech stack

| Layer | Technology |
|---|---|
| Frontend | React 18 + Vite + Tailwind CSS + Zustand |
| Backend | FastAPI + Uvicorn (async) + Pydantic v2 |
| AI / Agents | LangGraph StateGraph + LangChain LCEL + Claude Sonnet |
| RAG | ChromaDB + HyDE + MMR + Cross-encoder + Corrective RAG loop |
| Database | SQLite via aiosqlite + LangGraph AsyncSqliteSaver |
| Observability | LangSmith (full trace per run, streamed to UI) |
| MCP servers | EDGAR · yfinance · Brave · Python REPL |
| Agentic coding | Claude Code — SPEC.md, /commands, skills, hooks |
| Deploy | Vercel (frontend) + Render (backend) |

---

## Repo structure

```
FinSight/
├── backend/              FastAPI app
│   ├── main.py           App entrypoint, routers registered here
│   ├── scripts/          DB init and one-off utilities
│   │   └── init_db.py
│   ├── tests/            pytest suites
│   └── pyproject.toml    uv-managed dependencies
├── agents/               LangGraph graph, nodes, RAG pipeline, tools
│   └── __init__.py       (nodes/, rag/, tools/ to be scaffolded)
├── frontend/             React + Vite dashboard
│   └── src/
│       ├── App.tsx
│       └── main.tsx
├── Makefile              All dev commands (source of truth)
├── pnpm-workspace.yaml   Monorepo workspace
├── render.yaml           Render deployment config
├── .env.example          Required env vars (copy → .env)
└── CLAUDE.md             ← this file
```

> Note: `SPEC.md` will live at `claude-code/SPEC.md` once that directory is scaffolded.

---

## How to run

```bash
# Install everything
make install

# Initialise SQLite database (idempotent)
make db-init

# Start servers (two terminals)
make dev-backend     # FastAPI on http://localhost:8000
make dev-frontend    # React Vite on http://localhost:5173
```

Other useful targets:

```bash
make test            # pytest + vitest
make lint            # ruff + eslint/prettier
make ingest-docs     # ingest financial docs into ChromaDB
make db-reset        # drop and re-init finsight.db
```

---

## Coding conventions

**Python (backend + agents)**
- Package manager: `uv` — add deps with `uv add <pkg>`, never `pip install`
- Linter/formatter: `ruff` — run `make lint-backend` before committing
- All FastAPI route handlers must be `async def`; use `await` throughout
- Pydantic v2 schemas for all request/response bodies

**JavaScript / TypeScript (frontend)**
- Package manager: `pnpm` — never use `npm` or `yarn`
- Linter: `eslint` + `prettier` — run `make lint-frontend` before committing
- State management: Zustand (no Redux)

**Git commits**
- Prefix: `feat:` / `fix:` / `chore:` / `docs:` / `test:`
- Keep subject line ≤ 72 chars

---

## Key files to know

| File | Purpose |
|---|---|
| `backend/main.py` | FastAPI app factory, router registration |
| `backend/scripts/init_db.py` | Creates SQLite schema (idempotent) |
| `agents/__init__.py` | Agents package root |
| `Makefile` | Canonical commands — check here before running anything manually |
| `.env.example` | Documents every required env var |
| `claude-code/SPEC.md` | Full feature specification (to be created Day 2) |

---

## Current status

**Day 2** — monorepo scaffold complete. Building `SPEC.md` next.

Completed:
- [x] Monorepo layout (backend / agents / frontend)
- [x] FastAPI skeleton with health endpoint
- [x] React + Vite + Tailwind frontend scaffold
- [x] SQLite init script
- [x] Makefile with all dev targets
- [x] `.env.example` with all required vars
- [x] `render.yaml` deploy config

Up next:
- [ ] `claude-code/SPEC.md` — full feature specification
- [ ] LangGraph StateGraph skeleton in `agents/`
- [ ] ChromaDB RAG pipeline in `agents/rag/`
- [ ] WebSocket endpoint in `backend/`

---

## Never do

- **Never mutate LangGraph state in place** — always return a new state dict or use `operator.add` reducers; in-place mutation silently breaks the graph.
- **Never use synchronous calls in async FastAPI routes** — no `requests.get()`, no blocking I/O; use `httpx.AsyncClient`, `aiofiles`, or `asyncio.to_thread()`.
- **Never hardcode API keys** — all secrets go in `.env` and are read via `os.environ` or `pydantic-settings`; `.env` is in `.gitignore`.
- **Never install Python packages with pip directly** — use `uv add` so `pyproject.toml` stays in sync.
- **Never use `npm` or `yarn`** — this repo uses `pnpm`; running another package manager will corrupt the lockfile.
