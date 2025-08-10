from fastapi import APIRouter
from app.crud.tasks import TasksOrm
from app.models.tasks import Tasks


router = APIRouter(prefix="/tasks", tags=["tasks"])

@router.get("/")
async def get_tasks():
    return {"message": "success"}

@router.post("/")
async def post_task():
    task1 = Tasks(title="Первая задача", description="Описание первой задачи", is_done=False)
    task2 = Tasks(title="Вторая задача", description="Описание второй задачи", is_done=True)
    
    await TasksOrm.insert_task(task1)
    await TasksOrm.insert_task(task2)

    return {"status": "ok", "message": "task inserted"}