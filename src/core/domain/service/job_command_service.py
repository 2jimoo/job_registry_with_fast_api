from src.core.domain.port.in_.job_command_usecase import *
from src.core.domain.port.out.job_command_port import PersistJobPort


class JobCommandService(CreateJobUseCase):
    def __init__(self, persist_job_port: PersistJobPort):
        self.persist_job_port = persist_job_port

    def create(self, command: CreateJobCommand) -> Optional[Job]:
        raise self.persist_job_port.persist(
            Job(command.name, command.created_at, command.created_by, command.created_at, command.created_by)
        )
