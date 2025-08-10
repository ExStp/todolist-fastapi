from typing import Annotated
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.core.db import Base
import datetime
from sqlalchemy import text

intpk = Annotated[int, mapped_column(primary_key=True)]
created_at = Annotated[datetime.datetime, mapped_column(server_default=text("TIMEZONE('utc', now())"))]
updated_at = Annotated[datetime.datetime, mapped_column(
        server_default=text("TIMEZONE('utc', now())"),
        onupdate=datetime.datetime.utcnow,
    )]

class Tasks(Base):
    __tablename__ = "tasks"
    
    id: Mapped[intpk]
    title: Mapped[str]
    description: Mapped[str | None]
    is_done: Mapped[bool]