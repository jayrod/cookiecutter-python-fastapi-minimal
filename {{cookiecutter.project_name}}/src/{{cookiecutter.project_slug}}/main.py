from fastapi import Depends, FastAPI
from {{cookiecutter.project_slug}}.routers import users
from uuid import uuid4

app = FastAPI(
    title="{{cookiecutter.api_title}}",
    description="{{cookiecutter.description}}",
    version="{{cookiecutter.version}}"
)

app.include_router(users.router)

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/start")
async def start_action():
    #create an action_id
    uid = str(uuid4())
    return {"job_id": uid}

