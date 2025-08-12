from typing import Optional
from fastapi import APIRouter, HTTPException, Query
from app.crud.task import TaskOrm
from app.schemas.task import TaskPatchSchema, TaskPostSchema, TaskPutSchema, TaskSchema


router = APIRouter(prefix="/tasks", tags=["tasks"])


@router.get("/", name="Получить все задачи")
async def get_tasks() -> list[TaskSchema]:
    return await TaskOrm.get_tasks()


@router.get("/search", name="Поиск задач")
async def get_tasks_by_query(
    is_done: Optional[bool] = Query(None), title: Optional[str] = Query(None, max_length=50)
):
    tasks = await TaskOrm.get_tasks_by_query(is_done=is_done, title=title)
    if not tasks:
        raise HTTPException(status_code=404, detail="Задача не найдена")
    return tasks


@router.get("/{id}", name="Получить задачу по id")
async def get_task(id: int) -> TaskSchema:
    task = await TaskOrm.get_task(id)
    if not task:
        raise HTTPException(status_code=404, detail="Задача не найдена")
    return task


@router.post("/", name="Создать задачу")
async def post_task(task: TaskPostSchema) -> TaskSchema:
    return await TaskOrm.post_task(task)


@router.delete("/{id}", name="Удалить задачу по id")
async def delete_task(id: int) -> TaskSchema:
    deleted_task = await TaskOrm.delete_task(id)
    if not deleted_task:
        raise HTTPException(status_code=404, detail="Задача не найдена")
    return deleted_task


@router.put("/{id}", name="Обновить задачу по id")
async def put_task(id: int, task: TaskPutSchema) -> TaskSchema:
    updated_task = await TaskOrm.put_task(id, task)
    if not updated_task:
        raise HTTPException(status_code=404, detail="Задача не найдена")
    return updated_task


@router.patch("/{id}", name="Частично обновить задачу по id")
async def patch_task(id: int, task: TaskPatchSchema) -> TaskSchema:
    updated_task = await TaskOrm.patch_task(id, task)
    if not updated_task:
        raise HTTPException(status_code=404, detail="Задача не найдена")
    return updated_task
