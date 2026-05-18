"""
main.py — FinSight FastAPI application entry point.
"""

from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from scripts.init_db import init_db


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Startup: initialise SQLite. Shutdown: nothing needed for SQLite."""
    await init_db()
    print("✓ FinSight backend ready")
    yield


app = FastAPI(
    title="FinSight AI",
    description="Autonomous financial research agent — REST + WebSocket API",
    version="0.1.0",
    lifespan=lifespan,
)

# ── CORS ─────────────────────────────────────────────────────────────────────
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",   # Vite dev server
        "http://localhost:4173",   # Vite preview
        # Add your Vercel URL here after deployment:
        # "https://finsight.vercel.app",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ── Routers (stubbed — filled in Week 3–5) ───────────────────────────────────
# from routers import research, memory, websocket, health
# app.include_router(health.router)
# app.include_router(research.router, prefix="/api")
# app.include_router(memory.router,   prefix="/api")
# app.include_router(websocket.router)


# ── Health check ─────────────────────────────────────────────────────────────
@app.get("/api/health", tags=["system"])
async def health_check() -> dict:
    return {
        "status": "ok",
        "version": "0.1.0",
        "service": "finsight-backend",
    }


# ── Root ─────────────────────────────────────────────────────────────────────
@app.get("/", tags=["system"])
async def root() -> dict:
    return {"message": "FinSight AI backend — see /docs for API reference"}
