from abc import ABC, abstractmethod

from domain.entities.ProductBacklogItemsModels import ProductBacklogItemsCreate, ProductBacklogItemsUpdate
from domain.shared.operationResult import OperationResult
from domain.shared.queryResult import QueryResult


class IProductBacklogItemsRepository(ABC):
    @abstractmethod
    def insert_product_backlog_item(self, item: ProductBacklogItemsCreate, creator_id: int) -> OperationResult:
        raise NotImplementedError

    @abstractmethod
    def update_product_backlog_item(self, item: ProductBacklogItemsUpdate,
                                    modificator_id: int) -> OperationResult:
        raise NotImplementedError

    @abstractmethod
    def list_product_backlog_items(self, page_number: int, rows_per_page: int,
                                   pbi_id: int | None = None, pbi_parent_link: int | None = None,
                                   pbi_owner: int | None = None, pbi_status: int | None = None) -> QueryResult:
        raise NotImplementedError
