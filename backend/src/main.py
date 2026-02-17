"""FastAPI application entry point."""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os

# Create FastAPI application
app = FastAPI(
    title="Todo Backend API",
    description="Backend API for Todo Full-Stack Web Application (Phase II)",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
)

# CORS Configuration
CORS_ORIGINS = os.getenv("CORS_ORIGINS", "http://localhost:3000").split(",")

app.add_middleware(
    CORSMiddleware,
    allow_origins=CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health")
async def health_check() -> dict:
    """Health check endpoint."""
    return {"status": "healthy"}


@app.get("/")
async def root() -> dict:
    """Root endpoint."""
    return {
        "message": "Todo Backend API",
        "version": "1.0.0",
        "docs": "/docs",
    }


# Import and include routers
from src.api import auth, tasks

app.include_router(auth.router, prefix="/api/auth", tags=["auth"])
app.include_router(tasks.router, prefix="/api", tags=["tasks"])
