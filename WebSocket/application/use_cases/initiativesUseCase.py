from domain.entities.InitiativesModels import InitiativesCreate, InitiativesUpdate
from domain.interfaces.IInitiativesRepository import IInitiativesRepository


class InitiativeUseCase:
    def __init__(self, repository: IInitiativesRepository):
        self.repository = repository

    def create_initiative(self, initiative: InitiativesCreate, creator_id: int):
        return self.repository.insert_initiative(initiative, creator_id)

    def update_initiative(self, initiative: InitiativesUpdate, modificator_id: int):
        return self.repository.update_initiative(initiative, modificator_id)

    def list_initiatives(self, page_number: int, rows_per_page: int,
                         initiative_id: int | None = None, initiative_owner: int | None = None,
                         initiative_status: int | None = None):
        return self.repository.list_initiatives(
            page_number, rows_per_page, initiative_id, initiative_owner, initiative_status
        )
