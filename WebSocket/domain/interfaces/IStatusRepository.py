from abc import ABC, abstractmethod

from domain.entities.StatusModels import StatusCreate, StatusUpdate
from domain.shared.operationResult import OperationResult
from domain.shared.queryResult import QueryResult


class IStatusRepository(ABC):
    @abstractmethod
    def insert_status(self, status: StatusCreate, creator_id: int) -> OperationResult:
        raise NotImplementedError

    @abstractmethod
    def update_status(self, status: StatusUpdate, modificator_id: int) -> OperationResult:
        raise NotImplementedError

    @abstractmethod
    def list_statuses(self, page_number: int, rows_per_page: int,
                      status_id: int | None = None) -> QueryResult:
        raise NotImplementedError
