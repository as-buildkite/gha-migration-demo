"""A small FastAPI service with a few endpoints.

Kept intentionally simple so the CI pipeline (and its migration to
Buildkite) is the interesting part, not the app itself.
"""

from __future__ import annotations

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from . import __version__

app = FastAPI(title="GHA Migration Demo API", version=__version__)


class EchoRequest(BaseModel):
    message: str


class SumRequest(BaseModel):
    numbers: list[float]


@app.get("/health")
def health() -> dict[str, str]:
    """Liveness probe used by the container orchestrator."""
    return {"status": "ok", "version": __version__}


@app.get("/greet/{name}")
def greet(name: str) -> dict[str, str]:
    """Return a friendly greeting for the given name."""
    if not name.strip():
        raise HTTPException(status_code=400, detail="name must not be empty")
    return {"greeting": f"Hello, {name}!"}


@app.post("/sum")
def sum_numbers(payload: SumRequest) -> dict[str, float]:
    """Sum a list of numbers."""
    if not payload.numbers:
        raise HTTPException(status_code=400, detail="numbers must not be empty")
    return {"total": float(sum(payload.numbers))}


@app.post("/echo")
def echo(payload: EchoRequest) -> dict[str, str]:
    """Echo back the message the caller sent."""
    return {"echo": payload.message}
