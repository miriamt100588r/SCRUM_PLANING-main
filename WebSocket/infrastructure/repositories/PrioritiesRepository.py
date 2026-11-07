from domain.entities.PrioritiesModels import PrioritiesCreate, PrioritiesUpdate
from domain.interfaces.IPrioritiesRepository import IPrioritiesRepository
from infrastructure.database.base_repository import StoredProcedureRepository


class PrioritiesRepository(StoredProcedureRepository, IPrioritiesRepository):
    SP_NAME = "[SQM_CATALOGS].[USP_Priorities]"

    def insert_priority(self, priority: PrioritiesCreate, creator_id: int):
        return self.execute_procedure("I", {
            "i_priorityName": priority.priorityName,
            "i_priorityCreatorId": creator_id,
        })

    def update_priority(self, priority: PrioritiesUpdate, modificator_id: int):
        return self.execute_procedure("U", {
            "i_priorityId": priority.priorityId,
            "i_priorityName": priority.priorityName,
            "i_priorityModificatorId": modificator_id,
            "i_priorityEnable": priority.priorityEnable,
        })

    def list_priorities(self, page_number: int, rows_per_page: int, priority_id: int | None = None):
        return self.execute_procedure("S", {
            "i_priorityId": priority_id,
            "i_PageNumber": page_number,
            "i_RowsPerPage": rows_per_page,
        }, query=True)
