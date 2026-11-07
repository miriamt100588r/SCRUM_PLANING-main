from abc import ABC, abstractmethod

from domain.entities.BusinessValuesModels import BusinessValuesCreate, BusinessValuesUpdate
from domain.shared.operationResult import OperationResult
from domain.shared.queryResult import QueryResult


class IBusinessValuesRepository(ABC):
    @abstractmethod
    def insert_business_value(self, business_value: BusinessValuesCreate, creator_id: int) -> OperationResult:
        raise NotImplementedError

    @abstractmethod
    def update_business_value(self, business_value: BusinessValuesUpdate,
                              modificator_id: int) -> OperationResult:
        raise NotImplementedError

    @abstractmethod
    def list_business_values(self, page_number: int, rows_per_page: int,
                             business_value_id: int | None = None) -> QueryResult:
        raise NotImplementedError
