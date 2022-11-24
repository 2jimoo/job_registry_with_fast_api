import datetime
from abc import ABCMeta, abstractmethod
from time import time
from typing import Optional

import string_utils
from pydantic import BaseModel, validator

from src.core.domain.exceptions import InvalidArgumentError
from src.core.domain.model.job import Job


class CreateJobCommand(BaseModel):
    name: str
    created_at: time
    created_by: str

    @validator('name')
    def not_empty(cls, v):
        if not string_utils.is_full_string(v):
            raise InvalidArgumentError('Job name should not be blank')
        return v


class CreateJobUseCase(metaclass=ABCMeta):
    @abstractmethod
    def create(self, command: CreateJobCommand) -> Optional[Job]:
        raise NotImplementedError
