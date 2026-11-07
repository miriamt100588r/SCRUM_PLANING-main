from domain.entities.BusinessValuesModels import BusinessValuesCreate, BusinessValuesUpdate
from domain.interfaces.IBusinessValuesRepository import IBusinessValuesRepository


class BusinessValueUseCase:
    def __init__(self, repository: IBusinessValuesRepository):
        self.repository = repository

    def create_business_value(self, business_value: BusinessValuesCreate, creator_id: int):
        return self.repository.insert_business_value(business_value, creator_id)

    def update_business_value(self, business_value: BusinessValuesUpdate, modificator_id: int):
        return self.repository.update_business_value(business_value, modificator_id)

    def list_business_values(self, page_number: int, rows_per_page: int,
                             business_value_id: int | None = None):
        return self.repository.list_business_values(page_number, rows_per_page, business_value_id)
