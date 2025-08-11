import asyncio
from app.crud.base import BaseORM
from app.api.task import post_task
from app.models.task import TaskModel
from app.schemas.task import TaskPostSchema



async def main():
    task1 = TaskPostSchema(title="Реализовать все эндпоинты", description="Проект требует все эндпоинты", is_done=False)
    task2 = TaskPostSchema(title="Закоммитить изменения", description="Должна быть история", is_done=True)
    task3 = TaskPostSchema(title="Отдохнуть от работы", description="Можно выйти погулять", is_done=True)
    await BaseORM.create_tables()
    await post_task(task1)
    await post_task(task2)
    await post_task(task3)
    
asyncio.run(main())