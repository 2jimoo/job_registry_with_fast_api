from fastapi import FastAPI
from src.core.config.database import mongodb
from src.core.webapp.in_.job_router import job_router

app = FastAPI()
app.include_router(job_router)


@app.on_event("startup")
def on_app_start():
    mongodb.connect()


@app.on_event("shutdown")
def on_app_shutdown():
    mongodb.close()
