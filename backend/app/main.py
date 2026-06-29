from fastapi import FastAPI
from app.api.project_router import router as project_router
from app.auth.router import router as auth_router
from app.api.target_router import router as target_router

app = FastAPI(
    title="SentinelX API",
    version="0.1.0",
)

app.include_router(auth_router)
app.include_router(project_router)
app.include_router(target_router)

@app.get("/")
def root():
    return {
        "message": "Welcome to SentinelX API",
        "status": "running",
        "version": "0.1.0",
    }