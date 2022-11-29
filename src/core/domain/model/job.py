import datetime

from pydantic import BaseModel


class Job(BaseModel):
    name: str
    created_at: datetime.datetime
    created_by: str
    modified_at: datetime.datetime
    modified_by: str

    def __eq__(self, other: object) -> bool:
        return isinstance(other, Job) and self.name == other.name
