from pydantic import BaseModel
from datetime import datetime
from typing import Optional, List

class BusinessValuesBase(BaseModel):
	businessValueId: int
	businessValueName: str
	businessValueCreationDate: datetime
	businessValueCreatorId: int
	businessValueModificationDate: Optional[datetime] = None
	businessValueModificatorId: Optional[int] = None
	businessValueEnable: bool

class BusinessValuesCreate(BaseModel):
    businessValueName: str
    businessValueCreatorId: int

class BusinessValuesUpdate(BaseModel):
    businessValueId: int
    businessValueName: Optional[str] = None
    businessValueModificationDate: Optional[datetime] = None
    businessValueModificatorId: Optional[int] = None
    businessValueEnable: Optional[bool] = None