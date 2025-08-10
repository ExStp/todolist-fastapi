from app.models.tasks import Tasks
from app.core.db import async_session_factory

class TasksOrm:
    
    async def insert_task(task: Tasks):
        async with async_session_factory() as session:
            session.add(task)
            await session.commit()