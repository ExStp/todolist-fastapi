import asyncio
from app.crud.base import BaseORM
from app.api.task import post_task
from app.schemas.task import TaskPostSchema


async def init_create_tables():
    tasks = [
        TaskPostSchema(
            title="Подготовить документацию",
            description="Описать API в Swagger",
            is_done=False,
        ),
        TaskPostSchema(
            title="Написать тесты",
            description="Покрыть сервис unit-тестами",
            is_done=False,
        ),
        TaskPostSchema(
            title="Сделать деплой",
            description="Развернуть проект на сервере",
            is_done=True,
        ),
        TaskPostSchema(
            title="Настроить CI/CD",
            description="Добавить GitHub Actions для автоматического деплоя",
            is_done=False,
        ),
        TaskPostSchema(
            title="Проверить логи сервера",
            description="Исключить критические ошибки",
            is_done=True,
        ),
        TaskPostSchema(
            title="Рефакторинг кода",
            description="Улучшить читаемость и убрать дублирование",
            is_done=False,
        ),
        TaskPostSchema(
            title="Обновить зависимости",
            description="Обновить пакеты через Poetry",
            is_done=True,
        ),
        TaskPostSchema(
            title="Провести код-ревью",
            description="Проверить PR от коллеги",
            is_done=False,
        ),
        TaskPostSchema(
            title="Написать инструкцию по запуску",
            description="README.md с шагами установки",
            is_done=True,
        ),
        TaskPostSchema(
            title="Сделать резервную копию БД",
            description="Выгрузить дамп PostgreSQL",
            is_done=True,
        ),
        TaskPostSchema(
            title="Оптимизировать запросы",
            description="Использовать индексы и оптимизировать SQL",
            is_done=False,
        ),
        TaskPostSchema(
            title="Реализовать авторизацию",
            description="JWT + refresh токены",
            is_done=False,
        ),
        TaskPostSchema(
            title="Добавить логирование",
            description="Логировать ошибки и события",
            is_done=True,
        ),
        TaskPostSchema(
            title="Проверить фронтенд",
            description="Убедиться, что запросы корректно работают",
            is_done=True,
        ),
        TaskPostSchema(
            title="Составить план спринта",
            description="Определить задачи на ближайшие 2 недели",
            is_done=False,
        ),
    ]

    await BaseORM.create_tables()
    for task in tasks:
        await post_task(task)