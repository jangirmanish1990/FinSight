# FinSight — Makefile
# Usage: make <target>
# Requires: uv (Python), pnpm (Node), git

.PHONY: help dev-backend dev-frontend db-init db-reset \
        test test-backend test-frontend lint lint-backend lint-frontend \
        install install-backend install-frontend \
        ingest-docs claude-session

# ── Default ───────────────────────────────────────────────────────────────────
help:
	@echo ""
	@echo "  FinSight — available targets"
	@echo ""
	@echo "  Dev"
	@echo "    make dev-backend      Start FastAPI on :8000 (hot-reload)"
	@echo "    make dev-frontend     Start React Vite on :5173 (HMR)"
	@echo ""
	@echo "  Database"
	@echo "    make db-init          Create SQLite tables (idempotent)"
	@echo "    make db-reset         Drop finsight.db and re-init"
	@echo ""
	@echo "  Tests"
	@echo "    make test             Run all tests (backend + frontend)"
	@echo "    make test-backend     pytest only"
	@echo "    make test-frontend    vitest only"
	@echo ""
	@echo "  Lint"
	@echo "    make lint             Lint everything"
	@echo "    make lint-backend     ruff check + ruff format"
	@echo "    make lint-frontend    eslint + prettier check"
	@echo ""
	@echo "  Install"
	@echo "    make install          Install all dependencies (backend + frontend)"
	@echo ""
	@echo "  Docs"
	@echo "    make ingest-docs      Ingest financial documents into ChromaDB"
	@echo ""

# ── Dev servers ───────────────────────────────────────────────────────────────
dev-backend:
	@echo ">> Starting FastAPI on http://localhost:8000"
	cd backend && uv run uvicorn main:app --reload --host 0.0.0.0 --port 8000

dev-frontend:
	@echo ">> Starting React Vite on http://localhost:5173"
	cd frontend && pnpm dev

# ── Database ──────────────────────────────────────────────────────────────────
db-init:
	@echo ">> Initialising SQLite database"
	cd backend && uv run python scripts/init_db.py

db-reset:
	@echo ">> Resetting SQLite database"
	@rm -f backend/finsight.db backend/finsight.db-shm backend/finsight.db-wal
	@$(MAKE) db-init

# ── Tests ─────────────────────────────────────────────────────────────────────
test: test-backend test-frontend

test-backend:
	@echo ">> Running backend tests (pytest)"
	cd backend && uv run pytest tests/ -v --tb=short

test-frontend:
	@echo ">> Running frontend tests (vitest)"
	cd frontend && pnpm vitest run

# ── Lint ──────────────────────────────────────────────────────────────────────
lint: lint-backend lint-frontend

lint-backend:
	@echo ">> Linting backend (ruff)"
	cd backend && uv run ruff check . --fix
	cd backend && uv run ruff format .

lint-frontend:
	@echo ">> Linting frontend (eslint + prettier)"
	cd frontend && pnpm eslint src/ --fix
	cd frontend && pnpm prettier --write src/

# ── Install ───────────────────────────────────────────────────────────────────
install: install-backend install-frontend

install-backend:
	@echo ">> Installing backend dependencies (uv)"
	cd backend && uv sync

install-frontend:
	@echo ">> Installing frontend dependencies (pnpm)"
	cd frontend && pnpm install

# ── RAG ingestion ─────────────────────────────────────────────────────────────
ingest-docs:
	@echo ">> Ingesting documents into ChromaDB"
	cd backend && uv run python agents/rag/ingest.py

# ── Claude Code ───────────────────────────────────────────────────────────────
claude-session:
	@echo ">> Starting Claude Code session"
	claude
