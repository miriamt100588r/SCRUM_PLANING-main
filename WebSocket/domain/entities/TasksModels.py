from pydantic import BaseModel
from datetime import datetime, date
from decimal import Decimal
from typing import Optional


class TasksBase(BaseModel):
    taskId: int
    taskSummary: str
    taskDescription: str
    taskOwner: int
    taskParentLink: int
    taskOriginalEstimate: Optional[Decimal] = None
    taskCompletedWork: Optional[Decimal] = None
    taskRemaningWork: Optional[Decimal] = None
    taskStartDate: Optional[date] = None
    taskCompletedDate: Optional[date] = None
    taskDueDate: Optional[date] = None
    taskActivityType: Optional[int] = None
    taskCreationDate: datetime
    taskCreatorId: int
    taskModificationDate: Optional[datetime] = None
    taskModificatorId: Optional[int] = None
    taskStatus: int


class TasksCreate(BaseModel):
    taskSummary: str
    taskDescription: str
    taskOwner: int
    taskParentLink: int
    taskOriginalEstimate: Optional[Decimal] = None
    taskCompletedWork: Optional[Decimal] = None
    taskRemaningWork: Optional[Decimal] = None
    taskStartDate: Optional[date] = None
    taskCompletedDate: Optional[date] = None
    taskDueDate: Optional[date] = None
    taskActivityType: Optional[int] = None
    taskCreatorId: int
    taskStatus: int


class TasksUpdate(BaseModel):
    taskId: int
    taskSummary: Optional[str] = None
    taskDescription: Optional[str] = None
    taskOwner: Optional[int] = None
    taskParentLink: Optional[int] = None
    taskOriginalEstimate: Optional[Decimal] = None
    taskCompletedWork: Optional[Decimal] = None
    taskRemaningWork: Optional[Decimal] = None
    taskStartDate: Optional[date] = None
    taskCompletedDate: Optional[date] = None
    taskDueDate: Optional[date] = None
    taskActivityType: Optional[int] = None
    taskModificationDate: Optional[datetime] = None
    taskModificatorId: Optional[int] = None
    taskStatus: Optional[int] = None