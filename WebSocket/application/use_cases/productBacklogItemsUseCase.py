from domain.entities.ProductBacklogItemsModels import ProductBacklogItemsCreate, ProductBacklogItemsUpdate
from domain.interfaces.IProductBacklogItemsRepository import IProductBacklogItemsRepository


class ProductBacklogItemUseCase:
    def __init__(self, repository: IProductBacklogItemsRepository):
        self.repository = repository

    def create_product_backlog_item(self, item: ProductBacklogItemsCreate, creator_id: int):
        return self.repository.insert_product_backlog_item(item, creator_id)

    def update_product_backlog_item(self, item: ProductBacklogItemsUpdate, modificator_id: int):
        return self.repository.update_product_backlog_item(item, modificator_id)

    def list_product_backlog_items(self, page_number: int, rows_per_page: int,
                                   pbi_id: int | None = None, pbi_parent_link: int | None = None,
                                   pbi_owner: int | None = None, pbi_status: int | None = None):
        return self.repository.list_product_backlog_items(
            page_number, rows_per_page, pbi_id, pbi_parent_link, pbi_owner, pbi_status
        )
