from fastapi import FastAPI
from app.api.task import router as task_router
from fastapi.middleware.cors import CORSMiddleware
from app.core.init_db import init_create_tables

app = FastAPI(title="api")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(task_router)

@app.on_event("startup")
async def startup_event():
    await init_create_tables()

@app.get("/")
async def root():
    return {"message": "success"}
