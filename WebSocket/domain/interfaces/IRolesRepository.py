from abc import ABC, abstractmethod

from domain.entities.RolesModels import RolesCreate, RolesUpdate
from domain.shared.operationResult import OperationResult
from domain.shared.queryResult import QueryResult


class IRolesRepository(ABC):
    @abstractmethod
    def insert_role(self, role: RolesCreate, creator_id: int) -> OperationResult:
        raise NotImplementedError

    @abstractmethod
    def update_role(self, role: RolesUpdate, modificator_id: int) -> OperationResult:
        raise NotImplementedError

    @abstractmethod
    def list_roles(self, page_number: int, rows_per_page: int,
                   role_id: int | None = None) -> QueryResult:
        raise NotImplementedError
