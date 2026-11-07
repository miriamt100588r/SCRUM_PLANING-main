from domain.entities.ProductBacklogItemsModels import ProductBacklogItemsCreate, ProductBacklogItemsUpdate
from domain.interfaces.IProductBacklogItemsRepository import IProductBacklogItemsRepository
from infrastructure.database.base_repository import StoredProcedureRepository


class ProductBacklogItemsRepository(StoredProcedureRepository, IProductBacklogItemsRepository):
    SP_NAME = "[SQM_GENERAL].[USP_ProductBacklogItems]"

    def insert_product_backlog_item(self, item: ProductBacklogItemsCreate, creator_id: int):
        return self.execute_procedure("I", {
            "i_PBISummary": item.PBISummary,
            "i_PBIDescription": item.PBIDescription,
            "i_PBIsAcceptanceCriteria": item.PBIsAcceptanceCriteria,
            "i_PBIOwner": item.PBIOwner,
            "i_PBIParentLink": item.PBIParentLink,
            "i_PBIStoryPoint": item.PBIStoryPoint,
            "i_PBIStartDate": item.PBIStartDate,
            "i_PBIDueDate": item.PBIDueDate,
            "i_PBIPriority": item.PBIPriority,
            "i_PBICreatorId": creator_id,
            "i_PBIStatus": item.PBIStatus,
        })

    def update_product_backlog_item(self, item: ProductBacklogItemsUpdate, modificator_id: int):
        return self.execute_procedure("U", {
            "i_PBIId": item.PBIId,
            "i_PBISummary": item.PBISummary,
            "i_PBIDescription": item.PBIDescription,
            "i_PBIsAcceptanceCriteria": item.PBIsAcceptanceCriteria,
            "i_PBIOwner": item.PBIOwner,
            "i_PBIParentLink": item.PBIParentLink,
            "i_PBIStoryPoint": item.PBIStoryPoint,
            "i_PBIStartDate": item.PBIStartDate,
            "i_PBIDueDate": item.PBIDueDate,
            "i_PBIPriority": item.PBIPriority,
            "i_PBIModificatorId": modificator_id,
            "i_PBIStatus": item.PBIStatus,
        })

    def list_product_backlog_items(self, page_number: int, rows_per_page: int,
                                   pbi_id: int | None = None, pbi_parent_link: int | None = None,
                                   pbi_owner: int | None = None, pbi_status: int | None = None):
        return self.execute_procedure("S", {
            "i_PBIId": pbi_id,
            "i_PBIParentLink": pbi_parent_link,
            "i_PBIOwner": pbi_owner,
            "i_PBIStatus": pbi_status,
            "i_PageNumber": page_number,
            "i_RowsPerPage": rows_per_page,
        }, query=True)
