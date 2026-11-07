from abc import ABC, abstractmethod

from domain.entities.TaskCommentsModels import TaskCommentsCreate, TaskCommentsUpdate
from domain.shared.operationResult import OperationResult
from domain.shared.queryResult import QueryResult


class ITaskCommentsRepository(ABC):
    @abstractmethod
    def insert_task_comment(self, comment: TaskCommentsCreate, creator_id: int) -> OperationResult:
        raise NotImplementedError

    @abstractmethod
    def update_task_comment(self, comment: TaskCommentsUpdate, modificator_id: int) -> OperationResult:
        raise NotImplementedError

    @abstractmethod
    def list_task_comments(self, page_number: int, rows_per_page: int,
                           task_comment_id: int | None = None,
                           task_parent_link: int | None = None,
                           task_owner: int | None = None,
                           task_status: bool | None = None) -> QueryResult:
        raise NotImplementedError
