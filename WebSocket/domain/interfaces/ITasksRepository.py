from abc import ABC, abstractmethod

from domain.entities.TasksModels import TasksCreate, TasksUpdate
from domain.shared.operationResult import OperationResult
from domain.shared.queryResult import QueryResult


class ITasksRepository(ABC):
    @abstractmethod
    def insert_task(self, task: TasksCreate, creator_id: int) -> OperationResult:
        raise NotImplementedError

    @abstractmethod
    def update_task(self, task: TasksUpdate, modificator_id: int) -> OperationResult:
        raise NotImplementedError

    @abstractmethod
    def list_tasks(self, page_number: int, rows_per_page: int, task_id: int | None = None,
                   task_owner: int | None = None, task_parent_link: int | None = None,
                   task_status: int | None = None) -> QueryResult:
        raise NotImplementedError
