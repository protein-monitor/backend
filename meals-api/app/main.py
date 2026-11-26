from contextlib import asynccontextmanager

import psycopg
from fastapi import FastAPI, Response

from app.db import check_database


@asynccontextmanager
async def lifespan(app):
    check_database()  # raises an error if the database can't be reached
    print("Database: connected")
    yield


app = FastAPI(title="meals-api", lifespan=lifespan)


@app.get("/healthz")
def healthz(response: Response):
    try:
        check_database()
    except psycopg.Error:
        response.status_code = 503
        return {"status": "degraded", "database": "unreachable"}
    return {"status": "ok", "database": "ok"}
