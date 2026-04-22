from fastapi import FastAPI

app=FastAPI(title="Smart Budget API")
@app.get("/health")
def health():
    return {"status": "working", "message": "Independence is coming"}