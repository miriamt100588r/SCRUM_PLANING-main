from domain.entities.EpicsModels import EpicsCreate, EpicsUpdate
from domain.interfaces.IEpicsRepository import IEpicsRepository
from infrastructure.database.base_repository import StoredProcedureRepository


class EpicsRepository(StoredProcedureRepository, IEpicsRepository):
    SP_NAME = "[SQM_GENERAL].[USP_Epics]"

    def insert_epic(self, epic: EpicsCreate, creator_id: int):
        return self.execute_procedure("I", {
            "i_epicName": epic.epicName,
            "i_epicSummary": epic.epicSummary,
            "i_epicDescription": epic.epicDescription,
            "i_epicParentLink": epic.epicParentLink,
            "i_epicOwner": epic.epicOwner,
            "i_epicStartDate": epic.epicStartDate,
            "i_epicDueDate": epic.epicDueDate,
            "i_epicPriority": epic.epicPriority,
            "i_epicCreatorId": creator_id,
            "i_epicStatus": epic.epicStatus,
        })

    def update_epic(self, epic: EpicsUpdate, modificator_id: int):
        return self.execute_procedure("U", {
            "i_epicId": epic.epicId,
            "i_epicName": epic.epicName,
            "i_epicSummary": epic.epicSummary,
            "i_epicDescription": epic.epicDescription,
            "i_epicParentLink": epic.epicParentLink,
            "i_epicOwner": epic.epicOwner,
            "i_epicStartDate": epic.epicStartDate,
            "i_epicDueDate": epic.epicDueDate,
            "i_epicPriority": epic.epicPriority,
            "i_epicModificatorId": modificator_id,
            "i_epicStatus": epic.epicStatus,
        })

    def list_epics(self, page_number: int, rows_per_page: int, epic_id: int | None = None,
                   epic_parent_link: int | None = None, epic_owner: int | None = None,
                   epic_status: int | None = None):
        return self.execute_procedure("S", {
            "i_epicId": epic_id,
            "i_epicParentLink": epic_parent_link,
            "i_epicOwner": epic_owner,
            "i_epicStatus": epic_status,
            "i_PageNumber": page_number,
            "i_RowsPerPage": rows_per_page,
        }, query=True)
