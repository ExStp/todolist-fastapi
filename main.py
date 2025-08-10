from fastapi import FastAPI
from app.api.task import router as task_router

app = FastAPI(title="api")

app.include_router(task_router)

@app.get("/")
async def root():
    return {"message": "success"}