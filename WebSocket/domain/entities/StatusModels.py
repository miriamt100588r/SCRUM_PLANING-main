from pydantic import BaseModel
from datetime import datetime
from typing import Optional, List

class StatusBase(BaseModel):
	statusId: int
	statusName: str
	statusCreationDate: datetime
	statusCreatorId: int
	statusModificationDate: datetime
	statusModificatorId: Optional[int] = None
	statusEnable: bool

class StatusCreate(BaseModel):
    statusName: str

class StatusUpdate(BaseModel):
    statusId: int
    statusName: Optional[str] = None
    statusEnable: Optional[bool] = None

class LtsStatusBase(BaseModel):
    users: List[StatusBase]
