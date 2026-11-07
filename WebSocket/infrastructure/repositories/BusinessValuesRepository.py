from domain.entities.BusinessValuesModels import BusinessValuesCreate, BusinessValuesUpdate
from domain.interfaces.IBusinessValuesRepository import IBusinessValuesRepository
from infrastructure.database.base_repository import StoredProcedureRepository


class BusinessValuesRepository(StoredProcedureRepository, IBusinessValuesRepository):
    SP_NAME = "[SQM_CATALOGS].[USP_BusinessValues]"

    def insert_business_value(self, business_value: BusinessValuesCreate, creator_id: int):
        return self.execute_procedure("I", {
            "i_businessValueName": business_value.businessValueName,
            "i_businessValueCreatorId": creator_id,
        })

    def update_business_value(self, business_value: BusinessValuesUpdate, modificator_id: int):
        return self.execute_procedure("U", {
            "i_businessValueId": business_value.businessValueId,
            "i_businessValueName": business_value.businessValueName,
            "i_businessValueModificatorId": modificator_id,
            "i_businessValueEnable": business_value.businessValueEnable,
        })

    def list_business_values(self, page_number: int, rows_per_page: int, business_value_id: int | None = None):
        return self.execute_procedure("S", {
            "i_businessValueId": business_value_id,
            "i_PageNumber": page_number,
            "i_RowsPerPage": rows_per_page,
        }, query=True)
