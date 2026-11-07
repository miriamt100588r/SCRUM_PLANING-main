from domain.entities.RolesModels import RolesCreate, RolesUpdate
from domain.interfaces.IRolesRepository import IRolesRepository


class RoleUseCase:
    def __init__(self, repository: IRolesRepository):
        self.repository = repository

    def create_role(self, role: RolesCreate, creator_id: int):
        return self.repository.insert_role(role, creator_id)

    def update_role(self, role: RolesUpdate, modificator_id: int):
        return self.repository.update_role(role, modificator_id)

    def list_roles(self, page_number: int, rows_per_page: int, role_id: int | None = None):
        return self.repository.list_roles(page_number, rows_per_page, role_id)
