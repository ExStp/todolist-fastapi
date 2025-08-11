from pydantic import BaseModel, Field


class TaskSchema(BaseModel):
    id: int
    title: str
    description: str | None
    is_done: bool


class TaskPostSchema(BaseModel):
    title: str = Field(..., min_length=5, max_length=100)
    description: str | None = Field(None, max_length=500)

class TaskDeleteSchema(BaseModel):
    id: int