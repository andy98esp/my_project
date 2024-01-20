from application import init_sentry
init_sentry()

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def read_root():
    return {"Jenkins": "Push trigger only"}
