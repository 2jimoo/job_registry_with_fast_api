from abc import ABCMeta, abstractmethod
from typing import Optional

from src.core.domain.model.job import Job


class JobRepository(metaclass=ABCMeta):
    @abstractmethod
    async def find_by_name(self, name: str) -> Optional[Job]:
        raise NotImplementedError

    @abstractmethod
    async def persist(self, job: Job) -> Job:
        raise NotImplementedError
