from domain.entities.TasksModels import TasksCreate, TasksUpdate
from domain.interfaces.ITasksRepository import ITasksRepository
from infrastructure.database.base_repository import StoredProcedureRepository


class TasksRepository(StoredProcedureRepository, ITasksRepository):
    SP_NAME = "[SQM_GENERAL].[USP_Tasks]"

    def insert_task(self, task: TasksCreate, creator_id: int):
        return self.execute_procedure("I", {
            "i_taskSummary": task.taskSummary,
            "i_taskDescription": task.taskDescription,
            "i_taskOwner": task.taskOwner,
            "i_taskParentLink": task.taskParentLink,
            "i_taskOriginalEstimate": task.taskOriginalEstimate,
            "i_taskCompletedWork": task.taskCompletedWork,
            "i_taskRemaningWork": task.taskRemaningWork,
            "i_taskStartDate": task.taskStartDate,
            "i_taskCompletedDate": task.taskCompletedDate,
            "i_taskDueDate": task.taskDueDate,
            "i_taskActivityType": task.taskActivityType,
            "i_taskCreatorId": creator_id,
            "i_taskStatus": task.taskStatus,
        })

    def update_task(self, task: TasksUpdate, modificator_id: int):
        return self.execute_procedure("U", {
            "i_taskId": task.taskId,
            "i_taskSummary": task.taskSummary,
            "i_taskDescription": task.taskDescription,
            "i_taskOwner": task.taskOwner,
            "i_taskParentLink": task.taskParentLink,
            "i_taskOriginalEstimate": task.taskOriginalEstimate,
            "i_taskCompletedWork": task.taskCompletedWork,
            "i_taskRemaningWork": task.taskRemaningWork,
            "i_taskStartDate": task.taskStartDate,
            "i_taskCompletedDate": task.taskCompletedDate,
            "i_taskDueDate": task.taskDueDate,
            "i_taskActivityType": task.taskActivityType,
            "i_taskModificatorId": modificator_id,
            "i_taskStatus": task.taskStatus,
        })

    def list_tasks(self, page_number: int, rows_per_page: int, task_id: int | None = None,
                   task_owner: int | None = None, task_parent_link: int | None = None,
                   task_status: int | None = None):
        return self.execute_procedure("S", {
            "i_taskId": task_id,
            "i_taskOwner": task_owner,
            "i_taskParentLink": task_parent_link,
            "i_taskStatus": task_status,
            "i_PageNumber": page_number,
            "i_RowsPerPage": rows_per_page,
        }, query=True)
