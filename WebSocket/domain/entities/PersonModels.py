from pydantic import BaseModel
from datetime import datetime
from typing import Optional, List

class PersonBase(BaseModel):
    personId: int
    personFirstName: str
    personSecondName: Optional[str] = None
    personFirstSurname: str
    personSecondSurname: Optional[str] = None
    personBirthday: datetime
    personDNI: str
    personCreationDate: datetime
    personCreatorId: Optional[int] = None
    personModificationDate: Optional[datetime] = None
    personModificatorId: Optional[int] = None
    personEnable: bool

class PersonCreate(BaseModel):
    personFirstName: str
    personSecondName: Optional[str] = None
    personFirstSurname: str
    personSecondSurname: Optional[str] = None
    personBirthday: datetime
    personDNI: str

class PersonUpdate(BaseModel):
    personId: int
    personFirstName: Optional[str] = None
    personSecondName: Optional[str] = None
    personFirstSurname: Optional[str] = None
    personSecondSurname: Optional[str] = None
    personBirthday: Optional[datetime] = None
    personDNI: Optional[str] = None
    personModificationDate: Optional[datetime] = None
    personModificatorId: Optional[int] = None
    personEnable: Optional[bool] = None

class LtsPersonBase(BaseModel):
    users: List[PersonBase]