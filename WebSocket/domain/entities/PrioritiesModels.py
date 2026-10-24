from pydantic import BaseModel
from datetime import datetime
from typing import Optional, List

class PrioritiesBase(BaseModel):
	priorityId: int
	priorityName: str
	priorityCreationDate: datetime
	priorityCreatorId: int
	priorityModificationDate: Optional[datetime] = None
	priorityModificatorId: Optional[int] = None
	priorityEnable: bool

class PrioritiesCreate(BaseModel):
    priorityName: str
    priorityCreatorId: int

class PrioritiesUpdate(BaseModel):
    priorityId: int
    priorityName: Optional[str] = None
    priorityModificationDate: Optional[datetime] = None
    priorityModificatorId: Optional[int] = None
    priorityEnable: Optional[bool] = None