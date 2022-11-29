import datetime

from odmantic import Model


class JobModel(Model):
    name: str
    created_at: datetime.datetime
    created_by: str
    modified_at: datetime.datetime
    modified_by: str

    def to_document(self):
        return {
            '_id': self.name,
            'name': self.name,
            'created_at': self.created_at,
            'created_by': self.created_by,
            'modified_at': self.modified_at,
            'modified_by': self.modified_by
        }

    class Config:
        collection = "job"
