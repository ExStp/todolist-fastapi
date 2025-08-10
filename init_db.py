import asyncio
from app.crud.base import BaseORM
from app.api.task import post_task


async def main():
    await BaseORM.create_tables()
    await post_task()
    
asyncio.run(main())