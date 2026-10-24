from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class TaskCommentsBase(BaseModel):
    taskCommentId: int
    taskCommentParentLink: int
    taskCommentOwner: int
    taskCommentText: str
    taskCommentCreationDate: datetime
    taskCommentCreatorId: int
    taskCommentModificationDate: Optional[datetime] = None
    taskCommentModificatorId: Optional[int] = None
    taskCommentStatus: bool


class TaskCommentsCreate(BaseModel):
    taskCommentParentLink: int
    taskCommentOwner: int
    taskCommentText: str
    taskCommentCreatorId: int
    taskCommentStatus: bool


class TaskCommentsUpdate(BaseModel):
    taskCommentId: int
    taskCommentParentLink: Optional[int] = None
    taskCommentOwner: Optional[int] = None
    taskCommentText: Optional[str] = None
    taskCommentModificationDate: Optional[datetime] = None
    taskCommentModificatorId: Optional[int] = None
    taskCommentStatus: Optional[bool] = None