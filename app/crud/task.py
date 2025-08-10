from app.models.task import Task
from app.core.db import async_session_factory

class taskOrm:
    
    async def insert_task(task: Task):
        async with async_session_factory() as session:
            session.add(task)
            await session.commit()