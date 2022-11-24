from typing import Optional

from src.core.domain.model.job import Job
from src.core.domain.port.out.job_command_port import PersistJobPort
from src.core.webapp.out.mongo.repository.job_repository import JobRepository


class JobAdapter(PersistJobPort):
    def __init__(self, job_repository: JobRepository):
        self.job_repository = job_repository

    async def persist(self, job: Job) -> Optional[Job]:
        return await self.job_repository.persist(job)
