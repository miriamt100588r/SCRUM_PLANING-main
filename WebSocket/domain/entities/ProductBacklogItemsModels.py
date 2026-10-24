from pydantic import BaseModel
from datetime import datetime, date
from typing import Optional


class ProductBacklogItemsBase(BaseModel):
    PBIId: int
    PBISummary: str
    PBIDescription: str
    PBIsAcceptanceCriteria: str
    PBIOwner: int
    PBIParentLink: int
    PBIStoryPoint: Optional[int] = None
    PBIStartDate: Optional[date] = None
    PBIDueDate: Optional[date] = None
    PBIPriority: Optional[int] = None
    PBICreationDate: datetime
    PBICreatorId: int
    PBIModificationDate: Optional[datetime] = None
    PBIModificatorId: Optional[int] = None
    PBIStatus: int


class ProductBacklogItemsCreate(BaseModel):
    PBISummary: str
    PBIDescription: str
    PBIsAcceptanceCriteria: str
    PBIOwner: int
    PBIParentLink: int
    PBIStoryPoint: Optional[int] = None
    PBIStartDate: Optional[date] = None
    PBIDueDate: Optional[date] = None
    PBIPriority: Optional[int] = None
    PBICreatorId: int
    PBIStatus: int


class ProductBacklogItemsUpdate(BaseModel):
    PBIId: int
    PBISummary: Optional[str] = None
    PBIDescription: Optional[str] = None
    PBIsAcceptanceCriteria: Optional[str] = None
    PBIOwner: Optional[int] = None
    PBIParentLink: Optional[int] = None
    PBIStoryPoint: Optional[int] = None
    PBIStartDate: Optional[date] = None
    PBIDueDate: Optional[date] = None
    PBIPriority: Optional[int] = None
    PBIModificationDate: Optional[datetime] = None
    PBIModificatorId: Optional[int] = None
    PBIStatus: Optional[int] = None