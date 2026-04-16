from pathlib import Path

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel, Field

from app.hash_utils import detect_hash_type, verify_hash


class DetectRequest(BaseModel):
    hash_value: str = Field(..., min_length=1, max_length=300)


class VerifyRequest(BaseModel):
    hash_value: str = Field(..., min_length=1, max_length=300)
    plaintext: str = Field(..., min_length=1, max_length=300)


app = FastAPI(
    title="Lonewolf Hash Security Auditor",
    description="Safe hash analysis and verification for security auditing.",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

static_dir = Path(__file__).resolve().parent.parent / "static"
app.mount("/static", StaticFiles(directory=static_dir), name="static")


@app.get("/")
async def index() -> FileResponse:
    return FileResponse(static_dir / "index.html")


@app.post("/api/detect")
async def api_detect(payload: DetectRequest):
    hash_value = payload.hash_value.strip()
    if not hash_value:
        raise HTTPException(status_code=400, detail="hash_value cannot be empty")
    return detect_hash_type(hash_value)


@app.post("/api/verify")
async def api_verify(payload: VerifyRequest):
    hash_value = payload.hash_value.strip()
    plaintext = payload.plaintext

    if not hash_value:
        raise HTTPException(status_code=400, detail="hash_value cannot be empty")

    result = verify_hash(hash_value=hash_value, plaintext=plaintext)
    return result


@app.get("/health")
async def health():
    return {"status": "ok"}
