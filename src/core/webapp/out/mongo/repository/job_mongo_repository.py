from typing import Optional

from src.core.config.database import engine
from src.core.domain.model.job import Job
from src.core.webapp.out.mongo.repository.job_model import JobModel
from src.core.webapp.out.mongo.repository.job_repository import JobRepository


class JobMongoRepository(JobRepository):
    def __init__(self):
        self.engine = engine

    async def find_by_name(self, name: str) -> Optional[Job]:
        result = self.engine.find_one({"name": name})
        return self.map_to_domain(result)

    async def persist(self, job: Job) -> Job:
        job_model = self.map_to_entity(job)
        result = await self.engine.save(job_model)
        return self.map_to_domain(result)

    @staticmethod
    def map_to_entity(job: Job) -> JobModel:
        return JobModel(name=job.name, created_at=job.created_at, created_by=job.created_by,
                        modified_at=job.modified_at, modified_by=job.modified_by)

    @staticmethod
    def map_to_domain(result: JobModel) -> Job:
        return Job(name=result.name, created_at=result.created_at, created_by=result.created_by,
                   modified_at=result.modified_at, modified_by=result.modified_by)
