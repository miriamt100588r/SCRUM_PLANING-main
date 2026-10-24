from pydantic import BaseModel
from datetime import datetime, date
from typing import Optional


class InitiativesBase(BaseModel):
    initiativeId: int
    initiativeSummary: str
    initiativeDescription: str
    initiativeOwner: int
    initiativeGoals: Optional[str] = None
    initiativeBusinessValue: int
    initiativeTargetStart: Optional[date] = None
    initiativeTargetEnd: Optional[date] = None
    initiativeCreationDate: datetime
    initiativeCreatorId: int
    initiativeModificationDate: Optional[datetime] = None
    initiativeModificatorId: Optional[int] = None
    initiativeStatus: int


class InitiativesCreate(BaseModel):
    initiativeSummary: str
    initiativeDescription: str
    initiativeOwner: int
    initiativeGoals: Optional[str] = None
    initiativeBusinessValue: int
    initiativeTargetStart: Optional[date] = None
    initiativeTargetEnd: Optional[date] = None
    initiativeCreatorId: int
    initiativeStatus: int


class InitiativesUpdate(BaseModel):
    initiativeId: int
    initiativeSummary: Optional[str] = None
    initiativeDescription: Optional[str] = None
    initiativeOwner: Optional[int] = None
    initiativeGoals: Optional[str] = None
    initiativeBusinessValue: Optional[int] = None
    initiativeTargetStart: Optional[date] = None
    initiativeTargetEnd: Optional[date] = None
    initiativeModificationDate: Optional[datetime] = None
    initiativeModificatorId: Optional[int] = None
    initiativeStatus: Optional[int] = None