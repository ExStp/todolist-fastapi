from fastapi import FastAPI
from app.api.tasks import router as tasks_router

app = FastAPI(title="api")

app.include_router(tasks_router)

@app.get("/")
async def root():
    return {"message": "success"}