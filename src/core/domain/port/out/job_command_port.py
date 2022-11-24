from abc import ABCMeta, abstractmethod
from typing import Optional

from src.core.domain.model.job import Job


class PersistJobPort(metaclass=ABCMeta):
    @abstractmethod
    async def persist(self, job: Job) -> Optional[Job]:
        raise NotImplementedError
