import datetime
from abc import ABCMeta, abstractmethod
from typing import Optional

from pydantic import BaseModel

from src.core.domain.model.job import Job


class CreateJobCommand(BaseModel):
    name: str
    created_at: datetime.datetime
    created_by: str


class CreateJobUseCase(metaclass=ABCMeta):
    @abstractmethod
    async def create(self, command: CreateJobCommand) -> Optional[Job]:
        raise NotImplementedError
