from domain.entities.TaskCommentsModels import TaskCommentsCreate, TaskCommentsUpdate
from domain.interfaces.ITaskCommentsRepository import ITaskCommentsRepository
from infrastructure.database.base_repository import StoredProcedureRepository


class TaskCommentsRepository(StoredProcedureRepository, ITaskCommentsRepository):
    SP_NAME = "[SQM_GENERAL].[USP_TaskComments]"

    def insert_task_comment(self, comment: TaskCommentsCreate, creator_id: int):
        return self.execute_procedure("I", {
            "i_taskCommentParentLink": comment.taskCommentParentLink,
            "i_taskCommentOwner": comment.taskCommentOwner,
            "i_taskCommentText": comment.taskCommentText,
            "i_taskCommentCreatorId": creator_id,
            "i_taskCommentStatus": comment.taskCommentStatus,
        })

    def update_task_comment(self, comment: TaskCommentsUpdate, modificator_id: int):
        return self.execute_procedure("U", {
            "i_taskCommentId": comment.taskCommentId,
            "i_taskCommentParentLink": comment.taskCommentParentLink,
            "i_taskCommentOwner": comment.taskCommentOwner,
            "i_taskCommentText": comment.taskCommentText,
            "i_taskCommentModificatorId": modificator_id,
            "i_taskCommentStatus": comment.taskCommentStatus,
        })

    def list_task_comments(self, page_number: int, rows_per_page: int,
                           task_comment_id: int | None = None,
                           task_parent_link: int | None = None,
                           task_owner: int | None = None,
                           task_status: bool | None = None):
        return self.execute_procedure("S", {
            "i_taskCommentId": task_comment_id,
            "i_taskCommentParentLink": task_parent_link,
            "i_taskCommentOwner": task_owner,
            "i_taskCommentStatus": task_status,
            "i_PageNumber": page_number,
            "i_RowsPerPage": rows_per_page,
        }, query=True)
