from domain.entities.EpicsModels import EpicsCreate, EpicsUpdate
from domain.interfaces.IEpicsRepository import IEpicsRepository


class EpicUseCase:
    def __init__(self, repository: IEpicsRepository):
        self.repository = repository

    def create_epic(self, epic: EpicsCreate, creator_id: int):
        return self.repository.insert_epic(epic, creator_id)

    def update_epic(self, epic: EpicsUpdate, modificator_id: int):
        return self.repository.update_epic(epic, modificator_id)

    def list_epics(self, page_number: int, rows_per_page: int, epic_id: int | None = None,
                   epic_parent_link: int | None = None, epic_owner: int | None = None,
                   epic_status: int | None = None):
        return self.repository.list_epics(
            page_number, rows_per_page, epic_id, epic_parent_link, epic_owner, epic_status
        )
