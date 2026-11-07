from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, Query

from application.use_cases.activityTypesUseCase import ActivityTypeUseCase
from domain.entities.ActivityTypesModels import ActivityTypeCreate, ActivityTypeUpdate
from infrastructure.repositories.ActivityTypesRepository import ActivityTypesRepository
from presentation.security import get_admin_user
from presentation.states.generic_states import OperationResponse, QueryResponse


router = APIRouter(prefix="/websocket/activity-types", tags=["Catalogs - Activity Types"])


def get_activity_type_use_case() -> ActivityTypeUseCase:
    return ActivityTypeUseCase(ActivityTypesRepository())


ActivityTypeUseCaseDep = Annotated[ActivityTypeUseCase, Depends(get_activity_type_use_case)]
AdminUserDep = Annotated[dict[str, int | str], Depends(get_admin_user)]


@router.post("/create", response_model=OperationResponse, status_code=201)
def create_activity_type(activity_type: ActivityTypeCreate, use_case: ActivityTypeUseCaseDep,
                         admin_user: AdminUserDep):
    result = use_case.create_activity_type(activity_type, int(admin_user["sub"]))
    if result.status_code >= 400:
        raise HTTPException(status_code=result.status_code, detail=result.message_user)
    return result


@router.put("/update", response_model=OperationResponse)
def update_activity_type(activity_type: ActivityTypeUpdate, use_case: ActivityTypeUseCaseDep,
                         admin_user: AdminUserDep):
    result = use_case.update_activity_type(activity_type, int(admin_user["sub"]))
    if result.status_code >= 400:
        raise HTTPException(status_code=result.status_code, detail=result.message_user)
    return result


@router.get("/list", response_model=QueryResponse)
def list_activity_types(use_case: ActivityTypeUseCaseDep, admin_user: AdminUserDep,
                        page_number: Annotated[int, Query(ge=1)] = 1,
                        rows_per_page: Annotated[int, Query(ge=1, le=100)] = 10,
                        activity_type_id: int | None = None):
    result = use_case.list_activity_types(page_number, rows_per_page, activity_type_id)
    if result.status_code >= 400:
        raise HTTPException(status_code=result.status_code, detail=result.message_user)
    return result
