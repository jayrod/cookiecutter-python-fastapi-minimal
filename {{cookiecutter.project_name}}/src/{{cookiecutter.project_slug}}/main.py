from fastapi import Depends, FastAPI, BackgroundTasks
from {{cookiecutter.project_slug}}.routers import users
from uuid import uuid4
from starlette.responses import RedirectResponse

app = FastAPI(
    title="{{cookiecutter.api_title}}",
    description="{{cookiecutter.description}}",
    version="{{cookiecutter.version}}"
)

app.include_router(users.router)

def long_task(job_id: str):
    import time
    from pathlib import Path
    time.sleep(10)
    Path('/tmp', '{{cookiecutter.project_slug}}', job_id).mkdir(parents=True)

@app.get("/")
async def root():
    response = RedirectResponse(url='/docs')
    return response

@app.post("/tasks")
async def new_task(background_tasks: BackgroundTasks):
    #create an action_id
    uid = str(uuid4())
    background_tasks.add_task(long_task, uid)

    return {"job_id": uid}

