from sqlalchemy import select
from app.models.task import Task
from app.core.db import async_session_factory

class TaskOrm:
    
    async def get_tasks() -> list[Task]:
        async with async_session_factory() as session:
            result = await session.execute(select(Task))
            tasks = result.scalars().all()
            return tasks
            
    async def post_task(task: Task) -> Task:
        async with async_session_factory() as session:
            session.add(task)
            await session.commit()
            return Task