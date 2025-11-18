import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, EmailStr
from typing import Dict

app = FastAPI(title="WrapFury API", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {"status": "ok", "app": "WrapFury API"}


class QuoteIn(BaseModel):
    name: str
    email: EmailStr
    car: str
    wrap: str
    message: str | None = None

class QuoteOut(BaseModel):
    received: bool
    echo: Dict[str, str]


@app.post("/quote", response_model=QuoteOut)
async def quote(payload: QuoteIn) -> QuoteOut:
    # Placeholder persistence; in a full build we'd store to MongoDB
    return QuoteOut(received=True, echo=payload.model_dump())


@app.get("/test")
async def test():
    return {"backend": "✅ Running", "note": "DB not used for this simple quote demo"}


if __name__ == "__main__":
    import uvicorn
    port = int(os.getenv("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
