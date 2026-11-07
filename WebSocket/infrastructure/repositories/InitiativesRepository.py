from domain.entities.InitiativesModels import InitiativesCreate, InitiativesUpdate
from domain.interfaces.IInitiativesRepository import IInitiativesRepository
from infrastructure.database.base_repository import StoredProcedureRepository


class InitiativesRepository(StoredProcedureRepository, IInitiativesRepository):
    SP_NAME = "[SQM_GENERAL].[USP_Initiatives]"

    def insert_initiative(self, initiative: InitiativesCreate, creator_id: int):
        return self.execute_procedure("I", {
            "i_initiativeSummary": initiative.initiativeSummary,
            "i_initiativeDescription": initiative.initiativeDescription,
            "i_initiativeOwner": initiative.initiativeOwner,
            "i_initiativeGoals": initiative.initiativeGoals,
            "i_initiativeBusinessValue": initiative.initiativeBusinessValue,
            "i_initiativeTargetStart": initiative.initiativeTargetStart,
            "i_initiativeTargetEnd": initiative.initiativeTargetEnd,
            "i_initiativeCreatorId": creator_id,
            "i_initiativeStatus": initiative.initiativeStatus,
        })

    def update_initiative(self, initiative: InitiativesUpdate, modificator_id: int):
        return self.execute_procedure("U", {
            "i_initiativeId": initiative.initiativeId,
            "i_initiativeSummary": initiative.initiativeSummary,
            "i_initiativeDescription": initiative.initiativeDescription,
            "i_initiativeOwner": initiative.initiativeOwner,
            "i_initiativeGoals": initiative.initiativeGoals,
            "i_initiativeBusinessValue": initiative.initiativeBusinessValue,
            "i_initiativeTargetStart": initiative.initiativeTargetStart,
            "i_initiativeTargetEnd": initiative.initiativeTargetEnd,
            "i_initiativeModificatorId": modificator_id,
            "i_initiativeStatus": initiative.initiativeStatus,
        })

    def list_initiatives(self, page_number: int, rows_per_page: int, initiative_id: int | None = None,
                         initiative_owner: int | None = None, initiative_status: int | None = None):
        return self.execute_procedure("S", {
            "i_initiativeId": initiative_id,
            "i_initiativeOwner": initiative_owner,
            "i_initiativeStatus": initiative_status,
            "i_PageNumber": page_number,
            "i_RowsPerPage": rows_per_page,
        }, query=True)
