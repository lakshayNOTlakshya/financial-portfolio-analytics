from fastapi import FastAPI
from backend.database import engine, Base
import backend.models  # noqa: F401

app = FastAPI(
    title="Financial Portfolio Analytics Platform",
    version="0.1.0"
)

Base.metadata.create_all(bind=engine)

@app.get("/health")
def health_check():
    return {"status": "ok"}