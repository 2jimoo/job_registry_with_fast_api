import datetime

from odmantic import Model

from src.core.domain.model.job import Job


class JobModel(Model):
    name: str
    created_at: datetime
    created_by: str
    modified_at: datetime
    modified_by: str

    def of(self, job: Job):
        self.id = job.name
        self.name = job.name
        self.created_at = job.created_at
        self.created_by = job.created_by
        self.modified_at = job.modified_at
        self.modified_by = job.modified_by

    def to_document(self):
        return {
            '_id': self.id,
            'name': self.name,
            'created_at': self.created_at,
            'created_by': self.created_by,
            'modified_at': self.modified_at,
            'modified_by': self.modified_by
        }

    class Config:
        collection = "job"
