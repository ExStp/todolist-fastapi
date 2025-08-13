from pydantic import BaseModel, Field


class TaskSchema(BaseModel):
    id: int
    title: str
    description: str | None
    is_done: bool


class TaskPutSchema(BaseModel):
    title: str = Field(..., min_length=5, max_length=100)
    description: str | None = Field(None, max_length=500)
    is_done: bool = Field(False)


class TaskPatchSchema(BaseModel):
    title: str | None = Field(None, min_length=5, max_length=100)
    description: str | None = Field(None, max_length=500)
    is_done: bool | None = Field(False)


class TaskPostSchema(BaseModel):
    title: str = Field(..., min_length=5, max_length=50)
    description: str | None = Field(None, max_length=500)
