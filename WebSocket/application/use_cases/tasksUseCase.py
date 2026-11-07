from typing import Protocol
from domain.entities.TasksModels import TasksCreate, TasksUpdate


class TasksRepositoryProtocol(Protocol):

    def insert_task(self, task: TasksCreate, creator_id: int): ...

    def update_task(self, task: TasksUpdate, modificator_id: int): ...

    def list_tasks(
        self,
        page_number: int,
        rows_per_page: int,
        task_id: int | None = None,
        task_owner: int | None = None,
        task_parent_link: int | None = None,
        task_status: int | None = None,
    ): ...

class TaskUseCase:

    def __init__(self, repository: TasksRepositoryProtocol):
        self.repository = repository

    def create_task(self, task: TasksCreate, creator_id: int):
        return self.repository.insert_task(task, creator_id)

    def update_task(self, task: TasksUpdate, modificator_id: int):
        return self.repository.update_task(task, modificator_id)

    def list_tasks(
        self,
        page_number: int,
        rows_per_page: int,
        task_id: int | None = None,
        task_owner: int | None = None,
        task_parent_link: int | None = None,
        task_status: int | None = None,
    ):
        return self.repository.list_tasks(
            page_number=page_number,
            rows_per_page=rows_per_page,
            task_id=task_id,
            task_owner=task_owner,
            task_parent_link=task_parent_link,
            task_status=task_status,
        )
