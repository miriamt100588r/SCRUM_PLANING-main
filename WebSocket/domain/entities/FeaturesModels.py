from pydantic import BaseModel
from datetime import datetime, date
from typing import Optional


class FeaturesBase(BaseModel):
    featureId: int
    featureSummary: str
    featureDescription: str
    featuresAcceptanceCriteria: str
    featureParentLink: int
    featureOwner: int
    featureStartDate: Optional[date] = None
    featureDueDate: Optional[date] = None
    featurePriority: Optional[int] = None
    featureCreationDate: datetime
    featureCreatorId: int
    featureModificationDate: Optional[datetime] = None
    featureModificatorId: Optional[int] = None
    featureStatus: int


class FeaturesCreate(BaseModel):
    featureSummary: str
    featureDescription: str
    featuresAcceptanceCriteria: str
    featureParentLink: int
    featureOwner: int
    featureStartDate: Optional[date] = None
    featureDueDate: Optional[date] = None
    featurePriority: Optional[int] = None
    featureCreatorId: int
    featureStatus: int


class FeaturesUpdate(BaseModel):
    featureId: int
    featureSummary: Optional[str] = None
    featureDescription: Optional[str] = None
    featuresAcceptanceCriteria: Optional[str] = None
    featureParentLink: Optional[int] = None
    featureOwner: Optional[int] = None
    featureStartDate: Optional[date] = None
    featureDueDate: Optional[date] = None
    featurePriority: Optional[int] = None
    featureModificationDate: Optional[datetime] = None
    featureModificatorId: Optional[int] = None
    featureStatus: Optional[int] = None