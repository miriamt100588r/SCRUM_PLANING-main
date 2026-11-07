from domain.entities.UsersModels import UserCreate, UserLogin, UserUpdate
from domain.interfaces.IusersRepository import IUserRepository
from domain.shared.operationResult import OperationResult
from domain.shared.queryResult import QueryResult

from infrastructure.database.base_repository import StoredProcedureRepository


class UserRepository(StoredProcedureRepository, IUserRepository):
    SP_NAME = "[SQM_SECURITY].[USP_Users]"

    def insert_user(
        self,
        user: UserCreate,
        creator_id: int
    ) -> OperationResult:

        return self.execute_procedure("I", {
            "i_userFullName": user.userFullName,
            "i_userName": user.userName,
            "i_userEmail": user.userEmail,
            "i_userPassword": user.userPassword,
            "i_userRolId": user.userRolId,
            "i_userCreatorId": creator_id,
        })

    def update_user(
        self,
        user: UserUpdate,
        modificator_id: int
    ) -> OperationResult:

        return self.execute_procedure("U", {
            "i_userId": user.userId,
            "i_userFullName": user.userFullName,
            "i_userName": user.userName,
            "i_userEmail": user.userEmail,
            "i_userPassword": user.userPassword,
            "i_userRolId": user.userRolId,
            "i_userModificatorId": modificator_id,
            "i_userEnable": user.userEnable,
        })

    def authenticate_user(self, user: UserLogin) -> QueryResult:
        return self.execute_procedure("L", {
            "i_userName": user.userName,
            "i_userPassword": user.userPassword,
        }, query=True)

    def list_users(
        self,
        page_number: int = 1,
        rows_per_page: int = 10
    ) -> QueryResult:

        return self.execute_procedure("S", {
            "i_PageNumber": page_number,
            "i_RowsPerPage": rows_per_page,
        }, query=True)
