from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.exc import SQLAlchemyError
from app.models.task import TaskModel
from app.core.db import async_session_factory
from app.schemas.task import TaskPatchSchema, TaskPutSchema, TaskPostSchema


class TaskOrm:

    @staticmethod
    async def get_tasks() -> list[TaskModel]:
        async with async_session_factory() as session:
            result = await session.execute(select(TaskModel))
            return result.scalars().all()

    @staticmethod
    async def get_task(task_id: int) -> TaskModel:
        async with async_session_factory() as session:
            result = await session.execute(
                select(TaskModel).where(TaskModel.id == task_id)
            )
            return result.scalars().one_or_none()

    @staticmethod
    async def post_task(task_in: TaskPostSchema) -> TaskModel:
        async with async_session_factory() as session:
            task = TaskModel(**task_in.model_dump())
            session.add(task)
            await session.commit()
            await session.refresh(task)
            return task

    @staticmethod
    async def delete_task(task_id: int) -> TaskModel:
        async with async_session_factory() as session:
            result = await session.execute(
                select(TaskModel).where(TaskModel.id == task_id)
            )
            task_to_delete = result.scalars().one_or_none()

            if not task_to_delete:
                return None

            await session.delete(task_to_delete)
            await session.commit()
            return task_to_delete

    @staticmethod
    async def put_task(task_id: int, task_in: TaskPutSchema) -> TaskModel:
        async with async_session_factory() as session:
            task = await session.get(TaskModel, task_id)

            if not task:
                return None

            task.title = task_in.title
            task.description = task_in.description
            task.is_done = task_in.is_done

            await session.commit()
            await session.refresh(task)
            return task


    @staticmethod
    async def patch_task(task_id: int, task_in: TaskPatchSchema) -> TaskModel | None:
        async with async_session_factory() as session:
            task = await session.get(TaskModel, task_id)

            if not task:
                return None

            data = task_in.model_dump(exclude_unset=True)  # Берём только переданные поля

            for key, value in data.items():
                setattr(task, key, value)  # Обновляем поля объекта

            await session.commit()
            await session.refresh(task)
            return task
