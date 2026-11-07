from abc import ABC, abstractmethod

from domain.entities.InitiativesModels import InitiativesCreate, InitiativesUpdate
from domain.shared.operationResult import OperationResult
from domain.shared.queryResult import QueryResult


class IInitiativesRepository(ABC):
    @abstractmethod
    def insert_initiative(self, initiative: InitiativesCreate, creator_id: int) -> OperationResult:
        raise NotImplementedError

    @abstractmethod
    def update_initiative(self, initiative: InitiativesUpdate, modificator_id: int) -> OperationResult:
        raise NotImplementedError

    @abstractmethod
    def list_initiatives(self, page_number: int, rows_per_page: int,
                         initiative_id: int | None = None, initiative_owner: int | None = None,
                         initiative_status: int | None = None) -> QueryResult:
        raise NotImplementedError
