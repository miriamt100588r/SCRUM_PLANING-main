from abc import ABC, abstractmethod

from domain.entities.PrioritiesModels import PrioritiesCreate, PrioritiesUpdate
from domain.shared.operationResult import OperationResult
from domain.shared.queryResult import QueryResult


class IPrioritiesRepository(ABC):
    @abstractmethod
    def insert_priority(self, priority: PrioritiesCreate, creator_id: int) -> OperationResult:
        raise NotImplementedError

    @abstractmethod
    def update_priority(self, priority: PrioritiesUpdate, modificator_id: int) -> OperationResult:
        raise NotImplementedError

    @abstractmethod
    def list_priorities(self, page_number: int, rows_per_page: int,
                        priority_id: int | None = None) -> QueryResult:
        raise NotImplementedError
