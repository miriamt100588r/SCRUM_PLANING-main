from domain.entities.RolesModels import RolesCreate, RolesUpdate
from domain.interfaces.IRolesRepository import IRolesRepository
from infrastructure.database.base_repository import StoredProcedureRepository


class RolesRepository(StoredProcedureRepository, IRolesRepository):
    SP_NAME = "[SQM_SECURITY].[USP_Roles]"

    def insert_role(self, role: RolesCreate, creator_id: int):
        return self.execute_procedure("I", {
            "i_rolName": role.rolName,
            "i_rolCreatorId": creator_id,
        })

    def update_role(self, role: RolesUpdate, modificator_id: int):
        return self.execute_procedure("U", {
            "i_rolId": role.rolId,
            "i_rolName": role.rolName,
            "i_rolModificatorId": modificator_id,
            "i_rolEnable": role.rolEnable,
        })

    def list_roles(self, page_number: int, rows_per_page: int, role_id: int | None = None):
        return self.execute_procedure("S", {
            "i_rolId": role_id,
            "i_PageNumber": page_number,
            "i_RowsPerPage": rows_per_page,
        }, query=True)
