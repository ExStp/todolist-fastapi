from fastapi import APIRouter, HTTPException
from app.crud.task import TaskOrm
from app.schemas.task import TaskPostSchema, TaskSchema


router = APIRouter(prefix="/tasks", tags=["tasks"])


@router.get("/", name="Получить все задачи")
async def get_tasks() -> list[TaskSchema]:
    return await TaskOrm.get_tasks()


@router.post("/", name="Создать задачу")
async def post_task(task: TaskPostSchema) -> TaskSchema:
    return await TaskOrm.post_task(task)


@router.delete("/{id}", name="Удалить задачу по id")
async def delete_task(id: int) -> TaskSchema:
    deleted_task = await TaskOrm.delete_task(id)
    if not deleted_task:
        raise HTTPException(status_code=404, detail="Задача не найдена")
    return deleted_task