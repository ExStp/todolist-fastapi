from fastapi import APIRouter
from app.crud.task import taskOrm
from app.models.task import Task


router = APIRouter(prefix="/task", tags=["task"])

@router.get("/")
async def get_task():
    return {"message": "success"}

@router.post("/")
async def post_task():
    task1 = Task(title="Первая задача", description="Описание первой задачи", is_done=False)
    task2 = Task(title="Вторая задача", description="Описание второй задачи", is_done=True)
    
    await taskOrm.insert_task(task1)
    await taskOrm.insert_task(task2)

    return {"status": "ok", "message": "task inserted"}