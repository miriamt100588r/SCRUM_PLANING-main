from pydantic import BaseModel
from datetime import datetime
from typing import Optional, List

class RolesBase(BaseModel):
	rolId: int
	rolName: str
	rolCreationDate: datetime
	rolCreatorId: int
	rolModificationDate: datetime
	rolModificatorId: Optional[int] = None
	rolEnable: bool

class RolesCreate(BaseModel):
    rolName: str
    rolCreatorId: int

class RolesUpdate(BaseModel):
    rolId: int
    rolName: Optional[str] = None
    rolModificationDate: datetime
    rolModificatorId: Optional[int] = None
    rolEnable: Optional[bool] = None
