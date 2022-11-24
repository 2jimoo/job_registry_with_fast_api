import datetime


class Job:
    def __init__(self, name: str, created_at: datetime, created_by: str, modified_at: datetime, modified_by: str):
        self.name: str = name
        self.created_at: datetime = created_at
        self.created_by: str = created_by
        self.modified_at: datetime = modified_at
        self.modified_by = modified_by

    def __eq__(self, other: object) -> bool:
        return isinstance(other, Job) and self.name == other.name
