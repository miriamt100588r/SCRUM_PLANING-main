from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, Query

from application.use_cases.statusUseCase import StatusUseCase
from domain.entities.StatusModels import StatusCreate, StatusUpdate
from infrastructure.repositories.StatusRepository import StatusRepository
from presentation.security import get_admin_user
from presentation.states.generic_states import OperationResponse, QueryResponse


router = APIRouter(prefix="/websocket/status", tags=["Catalogs - Status"])


def get_status_use_case() -> StatusUseCase:
    return StatusUseCase(StatusRepository())


StatusUseCaseDep = Annotated[StatusUseCase, Depends(get_status_use_case)]
AdminUserDep = Annotated[dict[str, int | str], Depends(get_admin_user)]


@router.post("/create", response_model=OperationResponse, status_code=201)
def create_status(status: StatusCreate, use_case: StatusUseCaseDep, admin_user: AdminUserDep):
    result = use_case.create_status(status, int(admin_user["sub"]))
    if result.status_code >= 400:
        raise HTTPException(status_code=result.status_code, detail=result.message_user)
    return result


@router.put("/update", response_model=OperationResponse)
def update_status(status: StatusUpdate, use_case: StatusUseCaseDep, admin_user: AdminUserDep):
    result = use_case.update_status(status, int(admin_user["sub"]))
    if result.status_code >= 400:
        raise HTTPException(status_code=result.status_code, detail=result.message_user)
    return result


@router.get("/list", response_model=QueryResponse)
def list_statuses(use_case: StatusUseCaseDep, admin_user: AdminUserDep,
                  page_number: Annotated[int, Query(ge=1)] = 1,
                  rows_per_page: Annotated[int, Query(ge=1, le=100)] = 10,
                  status_id: int | None = None):
    result = use_case.list_statuses(page_number, rows_per_page, status_id)
    if result.status_code >= 400:
        raise HTTPException(status_code=result.status_code, detail=result.message_user)
    return result
