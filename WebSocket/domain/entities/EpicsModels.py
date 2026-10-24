from pydantic import BaseModel, Field, model_validator
from datetime import datetime, date
from typing import Optional


class EpicsBase(BaseModel):
    epicId: int
    epicName: str
    epicSummary: str
    epicDescription: str
    epicParentLink: int
    epicOwner: int
    epicStartDate: Optional[date] = None
    epicDueDate: Optional[date] = None
    epicPriority: Optional[int] = None
    epicCreationDate: datetime
    epicCreatorId: int
    epicModificationDate: Optional[datetime] = None
    epicModificatorId: Optional[int] = None
    epicStatus: int


class EpicsCreate(BaseModel):
    epicName: str = Field(..., max_length=100)
    epicSummary: str = Field(..., max_length=500)
    epicDescription: str = Field(..., max_length=4000)
    epicParentLink: int
    epicOwner: int
    epicStartDate: Optional[date] = None
    epicDueDate: Optional[date] = None
    epicPriority: Optional[int] = None
    epicCreatorId: int
    epicStatus: int

    #Validacion para asegurar que la fecha de inicio sea menor o igual a la fecha de vencimiento

    @model_validator(mode="after")
    def check_dates(self):
        if self.epicStartDate and self.epicDueDate:
            if self.epicDueDate < self.epicStartDate:
                raise ValueError("epicDueDate debe ser >= epicStartDate")
        return self


class EpicsUpdate(BaseModel):
    epicId: int
    epicName: Optional[str] = Field(None, max_length=100)
    epicSummary: Optional[str] = Field(None, max_length=500)
    epicDescription: Optional[str] = Field(None, max_length=4000)
    epicParentLink: Optional[int] = None
    epicOwner: Optional[int] = None
    epicStartDate: Optional[date] = None
    epicDueDate: Optional[date] = None
    epicPriority: Optional[int] = None
    epicModificationDate: Optional[datetime] = None
    epicModificatorId: Optional[int] = None
    epicStatus: Optional[int] = None