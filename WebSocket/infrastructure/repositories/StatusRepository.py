from domain.entities.StatusModels import StatusCreate, StatusUpdate
from domain.interfaces.IStatusRepository import IStatusRepository
from infrastructure.database.base_repository import StoredProcedureRepository


class StatusRepository(StoredProcedureRepository, IStatusRepository):
    SP_NAME = "[SQM_CATALOGS].[USP_Status]"

    def insert_status(self, status: StatusCreate, creator_id: int):
        return self.execute_procedure("I", {
            "i_statusName": status.statusName,
            "i_statusCreatorId": creator_id,
        })

    def update_status(self, status: StatusUpdate, modificator_id: int):
        return self.execute_procedure("U", {
            "i_statusId": status.statusId,
            "i_statusName": status.statusName,
            "i_statusModificatorId": modificator_id,
            "i_statusEnable": status.statusEnable,
        })

    def list_statuses(self, page_number: int, rows_per_page: int, status_id: int | None = None):
        return self.execute_procedure("S", {
            "i_statusId": status_id,
            "i_PageNumber": page_number,
            "i_RowsPerPage": rows_per_page,
        }, query=True)
