from fastapi import APIRouter
job_router = APIRouter(
    prefix="/jobs"
)


@job_router.get("/")
def test():

    return {"message": "Hello Job Router!"}



