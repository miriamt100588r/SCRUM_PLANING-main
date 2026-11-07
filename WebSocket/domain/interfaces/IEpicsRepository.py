from abc import ABC, abstractmethod

from domain.entities.EpicsModels import EpicsCreate, EpicsUpdate
from domain.shared.operationResult import OperationResult
from domain.shared.queryResult import QueryResult


class IEpicsRepository(ABC):
    @abstractmethod
    def insert_epic(self, epic: EpicsCreate, creator_id: int) -> OperationResult:
        raise NotImplementedError

    @abstractmethod
    def update_epic(self, epic: EpicsUpdate, modificator_id: int) -> OperationResult:
        raise NotImplementedError

    @abstractmethod
    def list_epics(self, page_number: int, rows_per_page: int, epic_id: int | None = None,
                   epic_parent_link: int | None = None, epic_owner: int | None = None,
                   epic_status: int | None = None) -> QueryResult:
        raise NotImplementedError
