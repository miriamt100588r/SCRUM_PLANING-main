from domain.entities.ActivityTypesModels import ActivityTypeCreate, ActivityTypeUpdate
from domain.interfaces.IActivityTypesRepository import IActivityTypesRepository
from infrastructure.database.base_repository import StoredProcedureRepository


class ActivityTypesRepository(StoredProcedureRepository, IActivityTypesRepository):
    SP_NAME = "[SQM_CATALOGS].[USP_ActivityTypes]"

    def insert_activity_type(self, activity_type: ActivityTypeCreate, creator_id: int):
        return self.execute_procedure("I", {
            "i_activityTypeName": activity_type.activityTypeName,
            "i_activityTypeCreatorId": creator_id,
        })

    def update_activity_type(self, activity_type: ActivityTypeUpdate, modificator_id: int):
        return self.execute_procedure("U", {
            "i_activityTypeId": activity_type.activityTypeId,
            "i_activityTypeName": activity_type.activityTypeName,
            "i_activityTypeModificatorId": modificator_id,
            "i_activityTypeEnable": activity_type.activityTypeEnable,
        })

    def list_activity_types(self, page_number: int, rows_per_page: int, activity_type_id: int | None = None):
        return self.execute_procedure("S", {
            "i_activityTypeId": activity_type_id,
            "i_PageNumber": page_number,
            "i_RowsPerPage": rows_per_page,
        }, query=True)
