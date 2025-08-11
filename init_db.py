import asyncio
from app.crud.base import BaseORM
from app.api.task import post_task
from app.models.task import Task



async def main():
    task1 = Task(title="Первая задача", description="Описание первой задачи", is_done=False)
    task2 = Task(title="Вторая задача", description="Описание второй задачи", is_done=True)
    
    await BaseORM.create_tables()
    await post_task(task1)
    await post_task(task2)
    
asyncio.run(main())