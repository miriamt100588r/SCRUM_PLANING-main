from pydantic import BaseModel
from datetime import datetime
from typing import Optional, List

class UserBase(BaseModel):
    userId: int
    userFullName: str
    userName: str
    userEmail: str
    userRolId: int
    userCreationDate: datetime
    userCreatorId: int
    userModificationDate: datetime
    userModificatorId: Optional[int] = None
    userEnable: bool


class UserCreate(BaseModel):
    userFullName: str
    userName: str
    userEmail: str
    userPassword: str
    userRolId: int
    userCreatorId: int

class UserUpdate(BaseModel):
    userId: int
    userFullName: Optional[str] = None
    userName: Optional[str] = None
    userEmail: Optional[str] = None
    userPassword: Optional[str] = None
    userRolId: Optional[int] = None
    userModificationDate: Optional[datetime] = None
    userModificatorId: int
    userEnable: Optional[bool] = None


class LtsUsers(BaseModel):
    users: List[UserBase]
