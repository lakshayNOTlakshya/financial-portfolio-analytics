from fastapi import FastAPI

app = FastAPI(
    title="Financial Portfolio Analytics Platform",
    description="API backend for portfolio returns, risk, and stress testing",
    version="0.1.0"
)

@app.get("/health")
def health_check():
    return {
        "status": "ok",
        "service": "portfolio-analytics-api"
    }