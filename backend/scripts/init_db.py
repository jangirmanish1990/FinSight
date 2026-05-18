"""
init_db.py — create all application tables if they don't exist.
Run via: uv run python scripts/init_db.py
Or:       make db-init
"""

import asyncio
import os
import sys
from pathlib import Path

import aiosqlite
from dotenv import load_dotenv

# Load .env from project root (two levels up from backend/scripts/)
load_dotenv(Path(__file__).parent.parent.parent / ".env")

DB_PATH = os.getenv("DATABASE_URL", "sqlite+aiosqlite:///./finsight.db")
# Strip the SQLAlchemy prefix if present
DB_FILE = DB_PATH.replace("sqlite+aiosqlite:///", "").replace("sqlite:///", "")


DDL = [
    # ── Run metadata ────────────────────────────────────────────────────────
    """
    CREATE TABLE IF NOT EXISTS runs (
        id           TEXT PRIMARY KEY,
        ticker       TEXT NOT NULL,
        status       TEXT NOT NULL DEFAULT 'pending',
        report       TEXT,          -- JSON string (ReportResponse)
        rag_grades   TEXT,          -- JSON string (List[RAGChunk])
        created_at   TEXT NOT NULL DEFAULT (datetime('now')),
        completed_at TEXT           -- NULL until done
    )
    """,
    "CREATE INDEX IF NOT EXISTS idx_runs_ticker ON runs(ticker)",
    "CREATE INDEX IF NOT EXISTS idx_runs_status ON runs(status)",

    # ── Per-ticker entity memory store ──────────────────────────────────────
    """
    CREATE TABLE IF NOT EXISTS entities (
        ticker     TEXT PRIMARY KEY,
        data       TEXT NOT NULL DEFAULT '{}',  -- JSON string
        updated_at TEXT NOT NULL DEFAULT (datetime('now'))
    )
    """,

    # ── User feedback ────────────────────────────────────────────────────────
    """
    CREATE TABLE IF NOT EXISTS feedback (
        id         TEXT PRIMARY KEY,
        run_id     TEXT NOT NULL REFERENCES runs(id),
        rating     INTEGER NOT NULL CHECK(rating BETWEEN 1 AND 5),
        note       TEXT,
        created_at TEXT NOT NULL DEFAULT (datetime('now'))
    )
    """,
    "CREATE INDEX IF NOT EXISTS idx_feedback_run ON feedback(run_id)",
]


async def init_db() -> None:
    db_path = Path(DB_FILE)
    db_path.parent.mkdir(parents=True, exist_ok=True)

    async with aiosqlite.connect(db_path) as db:
        await db.execute("PRAGMA journal_mode=WAL")
        await db.execute("PRAGMA foreign_keys=ON")
        for stmt in DDL:
            await db.execute(stmt)
        await db.commit()

    print(f"✓ Database initialised: {db_path.resolve()}")
    print("  Tables: runs, entities, feedback")
    print("  Note: LangGraph checkpoint tables are created by AsyncSqliteSaver.setup()")


if __name__ == "__main__":
    asyncio.run(init_db())
    sys.exit(0)
