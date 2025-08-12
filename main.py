from fastapi import FastAPI
from app.api.task import router as task_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="api")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(task_router)


@app.get("/")
async def root():
    return {"message": "success"}
