from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, Query

from application.use_cases.businessValuesUseCase import BusinessValueUseCase
from domain.entities.BusinessValuesModels import BusinessValuesCreate, BusinessValuesUpdate
from infrastructure.repositories.BusinessValuesRepository import BusinessValuesRepository
from presentation.security import get_admin_user
from presentation.states.generic_states import OperationResponse, QueryResponse


router = APIRouter(prefix="/websocket/business-values", tags=["Catalogs - Business Values"])


def get_business_value_use_case() -> BusinessValueUseCase:
    return BusinessValueUseCase(BusinessValuesRepository())


BusinessValueUseCaseDep = Annotated[BusinessValueUseCase, Depends(get_business_value_use_case)]
AdminUserDep = Annotated[dict[str, int | str], Depends(get_admin_user)]


@router.post("/create", response_model=OperationResponse, status_code=201)
def create_business_value(business_value: BusinessValuesCreate, use_case: BusinessValueUseCaseDep,
                          admin_user: AdminUserDep):
    result = use_case.create_business_value(business_value, int(admin_user["sub"]))
    if result.status_code >= 400:
        raise HTTPException(status_code=result.status_code, detail=result.message_user)
    return result


@router.put("/update", response_model=OperationResponse)
def update_business_value(business_value: BusinessValuesUpdate, use_case: BusinessValueUseCaseDep,
                          admin_user: AdminUserDep):
    result = use_case.update_business_value(business_value, int(admin_user["sub"]))
    if result.status_code >= 400:
        raise HTTPException(status_code=result.status_code, detail=result.message_user)
    return result


@router.get("/list", response_model=QueryResponse)
def list_business_values(use_case: BusinessValueUseCaseDep, admin_user: AdminUserDep,
                         page_number: Annotated[int, Query(ge=1)] = 1,
                         rows_per_page: Annotated[int, Query(ge=1, le=100)] = 10,
                         business_value_id: int | None = None):
    result = use_case.list_business_values(page_number, rows_per_page, business_value_id)
    if result.status_code >= 400:
        raise HTTPException(status_code=result.status_code, detail=result.message_user)
    return result
