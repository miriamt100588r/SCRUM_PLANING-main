from pydantic import BaseModel
from domain.entities.PersonModels import PersonCreate
from domain.entities.UsersModels import UserCreate

class UserProfileCreate(BaseModel):
    personData: PersonCreate
    userData: UserCreate