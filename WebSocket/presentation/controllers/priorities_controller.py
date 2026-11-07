from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, Query

from application.use_cases.prioritiesUseCase import PriorityUseCase
from domain.entities.PrioritiesModels import PrioritiesCreate, PrioritiesUpdate
from infrastructure.repositories.PrioritiesRepository import PrioritiesRepository
from presentation.security import get_admin_user
from presentation.states.generic_states import OperationResponse, QueryResponse


router = APIRouter(prefix="/websocket/priorities", tags=["Catalogs - Priorities"])


def get_priority_use_case() -> PriorityUseCase:
    return PriorityUseCase(PrioritiesRepository())


PriorityUseCaseDep = Annotated[PriorityUseCase, Depends(get_priority_use_case)]
AdminUserDep = Annotated[dict[str, int | str], Depends(get_admin_user)]


@router.post("/create", response_model=OperationResponse, status_code=201)
def create_priority(priority: PrioritiesCreate, use_case: PriorityUseCaseDep, admin_user: AdminUserDep):
    result = use_case.create_priority(priority, int(admin_user["sub"]))
    if result.status_code >= 400:
        raise HTTPException(status_code=result.status_code, detail=result.message_user)
    return result


@router.put("/update", response_model=OperationResponse)
def update_priority(priority: PrioritiesUpdate, use_case: PriorityUseCaseDep, admin_user: AdminUserDep):
    result = use_case.update_priority(priority, int(admin_user["sub"]))
    if result.status_code >= 400:
        raise HTTPException(status_code=result.status_code, detail=result.message_user)
    return result


@router.get("/list", response_model=QueryResponse)
def list_priorities(use_case: PriorityUseCaseDep, admin_user: AdminUserDep,
                    page_number: Annotated[int, Query(ge=1)] = 1,
                    rows_per_page: Annotated[int, Query(ge=1, le=100)] = 10,
                    priority_id: int | None = None):
    result = use_case.list_priorities(page_number, rows_per_page, priority_id)
    if result.status_code >= 400:
        raise HTTPException(status_code=result.status_code, detail=result.message_user)
    return result
