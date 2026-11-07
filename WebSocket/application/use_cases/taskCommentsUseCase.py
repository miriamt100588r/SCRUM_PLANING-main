from domain.entities.TaskCommentsModels import TaskCommentsCreate, TaskCommentsUpdate
from domain.interfaces.ITaskCommentsRepository import ITaskCommentsRepository


class TaskCommentUseCase:
    def __init__(self, repository: ITaskCommentsRepository):
        self.repository = repository

    def create_task_comment(self, comment: TaskCommentsCreate, creator_id: int):
        return self.repository.insert_task_comment(comment, creator_id)

    def update_task_comment(self, comment: TaskCommentsUpdate, modificator_id: int):
        return self.repository.update_task_comment(comment, modificator_id)

    def list_task_comments(self, page_number: int, rows_per_page: int,
                           task_comment_id: int | None = None,
                           task_parent_link: int | None = None,
                           task_owner: int | None = None,
                           task_status: bool | None = None):
        return self.repository.list_task_comments(
            page_number, rows_per_page, task_comment_id, task_parent_link, task_owner, task_status
        )
