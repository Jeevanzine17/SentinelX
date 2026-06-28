from fastapi import FastAPI

app = FastAPI(
    title="SentinelX API",
    description="AI-Powered Security Assessment Platform",
    version="0.1.0",
)

@app.get("/")
def root():
    return {
        "message": "Welcome to SentinelX API",
        "status": "running",
        "version": "0.1.0",
    }