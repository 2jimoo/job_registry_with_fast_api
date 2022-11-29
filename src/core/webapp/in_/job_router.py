from datetime import datetime

from fastapi import APIRouter, status, Depends
from pydantic import BaseModel

from src.core.domain.exceptions import UnexpectedRequestFailError
from src.core.domain.port.in_.job_command_usecase import CreateJobCommand
from src.core.domain.service.job_command_service import JobCommandService
from src.core.webapp.out.adapter.job_adapter import JobAdapter
from src.core.webapp.out.mongo.repository.job_mongo_repository import JobMongoRepository

job_router = APIRouter(
    prefix="/jobs"
)


# TODO add validator

class JobCreateRequest(BaseModel):
    name: str
    requester: str


class JobViewModel(BaseModel):
    name: str
    created_at: datetime
    created_by: str
    modified_at: datetime
    modified_by: str


@job_router.post(
    path='',
    response_model=JobViewModel,
    status_code=status.HTTP_201_CREATED
)
async def create(
        job_create_request: JobCreateRequest,
        job_repository: JobMongoRepository = Depends()):
    persist_job_port = JobAdapter(job_repository)
    create_job_use_case = JobCommandService(persist_job_port)
    job_created = await create_job_use_case.create(
        CreateJobCommand(
            name=job_create_request.name,
            created_at=datetime.utcnow(),
            created_by=job_create_request.requester
        ))
    if job_created:
        return JobViewModel(
            name=job_created.name,
            created_at=job_created.created_at,
            created_by=job_created.created_by,
            modified_at=job_created.modified_at,
            modified_by=job_created.modified_by
        )
    else:
        raise UnexpectedRequestFailError("Fail to create job.")


@job_router.get("/")
def test():
    return {"message": "Hello Job Router!"}
