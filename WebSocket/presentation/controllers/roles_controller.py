from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, Query

from application.use_cases.rolesUseCase import RoleUseCase
from domain.entities.RolesModels import RolesCreate, RolesUpdate
from infrastructure.repositories.RolesRepository import RolesRepository
from presentation.security import get_admin_user
from presentation.states.generic_states import OperationResponse, QueryResponse


router = APIRouter(prefix="/websocket/roles", tags=["Security - Roles"])


def get_role_use_case() -> RoleUseCase:
    return RoleUseCase(RolesRepository())


RoleUseCaseDep = Annotated[RoleUseCase, Depends(get_role_use_case)]
AdminUserDep = Annotated[dict[str, int | str], Depends(get_admin_user)]


@router.post("/create", response_model=OperationResponse, status_code=201)
def create_role(role: RolesCreate, use_case: RoleUseCaseDep, admin_user: AdminUserDep):
    result = use_case.create_role(role, int(admin_user["sub"]))
    if result.status_code >= 400:
        raise HTTPException(status_code=result.status_code, detail=result.message_user)
    return result


@router.put("/update", response_model=OperationResponse)
def update_role(role: RolesUpdate, use_case: RoleUseCaseDep, admin_user: AdminUserDep):
    result = use_case.update_role(role, int(admin_user["sub"]))
    if result.status_code >= 400:
        raise HTTPException(status_code=result.status_code, detail=result.message_user)
    return result


@router.get("/list", response_model=QueryResponse)
def list_roles(use_case: RoleUseCaseDep, admin_user: AdminUserDep,
               page_number: Annotated[int, Query(ge=1)] = 1,
               rows_per_page: Annotated[int, Query(ge=1, le=100)] = 10,
               role_id: int | None = None):
    result = use_case.list_roles(page_number, rows_per_page, role_id)
    if result.status_code >= 400:
        raise HTTPException(status_code=result.status_code, detail=result.message_user)
    return result
