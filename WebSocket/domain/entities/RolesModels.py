from pydantic import BaseModel
from datetime import datetime
from typing import Optional, List

class RolesBase(BaseModel):
	roleId: int
	roleName: str
	roleCreationDate: datetime
	roleCreatorId: int
	roleModificationDate: datetime
	roleModificatorId: Optional[int] = None
	roleEnable: bool

class RolesCreate(BaseModel):
    roleName: str
    roleCreatorId: int

class RolesUpdate(BaseModel):
    roleId: int
    roleName: Optional[str] = None
    roleModificationDate: datetime
    roleModificatorId: Optional[int] = None
    roleEnable: Optional[bool] = None