from fastapi import FastAPI

app = FastAPI(title="meals-api")


@app.get("/healthz")
def healthz():
    return {"status": "ok"}
