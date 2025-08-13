from typing import Annotated
from sqlalchemy.orm import Mapped, mapped_column
from app.core.db import Base
import datetime
from sqlalchemy import text

intpk = Annotated[int, mapped_column(primary_key=True)]
created_at = Annotated[datetime.datetime, mapped_column(server_default=text("TIMEZONE('utc', now())"))]
updated_at = Annotated[datetime.datetime, mapped_column(
        server_default=text("TIMEZONE('utc', now())"),
        onupdate=datetime.datetime.utcnow,
    )]

class TaskModel(Base):
    __tablename__ = "tasks"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str]
    description: Mapped[str | None]
    is_done: Mapped[bool] = mapped_column(default=False, nullable=False)
    created_at: Mapped[created_at]
    updated_at: Mapped[updated_at]