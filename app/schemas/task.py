from pydantic import BaseModel

class TaskSchema(BaseModel):
    id: int
    title: str
    description: str | None
    is_done: bool
    
class TaskPostSchema(BaseModel):
    title: str
    description: str | None