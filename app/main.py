from fastapi import FastAPI

app = FastAPI()

@app.get("/healthz")
def healthz():
    return {"ok": True}

@app.get("/api/hello")
def hello():
    return {"message": "hello from fastapi on home k8s"}
