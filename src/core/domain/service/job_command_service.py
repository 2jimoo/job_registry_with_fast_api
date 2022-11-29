from src.core.domain.port.in_.job_command_usecase import *
from src.core.domain.port.out.job_command_port import PersistJobPort


class JobCommandService(CreateJobUseCase):
    def __init__(self, persist_job_port: PersistJobPort):
        self.persist_job_port = persist_job_port

    async def create(self, command: CreateJobCommand) -> Optional[Job]:
        # TODO 이름 중복 확인
        return await self.persist_job_port.persist(
            Job(name=command.name, created_at=command.created_at, created_by=command.created_by,
                modified_at=command.created_at, modified_by=command.created_by)
        )
