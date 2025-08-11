from fastapi import APIRouter
from app.crud.task import TaskOrm
from app.schemas.task import TaskPostSchema, TaskSchema


router = APIRouter(prefix="/tasks", tags=["tasks"])

@router.get("/", name="Получить все задачи")
async def get_tasks() -> list[TaskSchema]:
    return await TaskOrm.get_tasks()

@router.post("/", name="Создать задачу")
async def post_task(task: TaskPostSchema):
    return await TaskOrm.post_task(task)