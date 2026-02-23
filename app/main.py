from fastapi import FastAPI
from contextlib import asynccontextmanager
from base.middleware import LoggingMiddleware



@asynccontextmanager    
async def lifespan(app: FastAPI):
    yield

app = FastAPI(
    title="Sample FastAPI",
    description="Sample FastAPI",
    version="0.1.0",
    lifespan=lifespan
)

app.add_middleware(LoggingMiddleware)

@app.get("/healthz")
def healthz():
    return {"ok": True}

@app.get("/api/hello")
def hello():
    return {"message": "hello from fastapi"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        app, 
        host="0.0.0.0", 
        port=8001,
        log_level="debug"
    )