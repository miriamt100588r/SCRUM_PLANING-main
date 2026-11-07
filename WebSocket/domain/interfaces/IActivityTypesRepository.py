from abc import ABC, abstractmethod

from domain.entities.ActivityTypesModels import ActivityTypeCreate, ActivityTypeUpdate
from domain.shared.operationResult import OperationResult
from domain.shared.queryResult import QueryResult


class IActivityTypesRepository(ABC):
    @abstractmethod
    def insert_activity_type(self, activity_type: ActivityTypeCreate, creator_id: int) -> OperationResult:
        raise NotImplementedError

    @abstractmethod
    def update_activity_type(self, activity_type: ActivityTypeUpdate,
                             modificator_id: int) -> OperationResult:
        raise NotImplementedError

    @abstractmethod
    def list_activity_types(self, page_number: int, rows_per_page: int,
                            activity_type_id: int | None = None) -> QueryResult:
        raise NotImplementedError
