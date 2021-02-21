from fastapi import APIRouter

router = APIRouter()


@router.get("/tasks/", tags=["tasks"])
async def read_tasks():
    return [{"username": "Rick"}, {"username": "Morty"}]

@router.post("/tasks/", tags=["tasks"])
async def create_task():
    return {"task_id" : "3"}


@router.get("/tasks/me", tags=["tasks"])
async def read_user_me():
    return {"username": "fakecurrentuser"}


@router.get("/tasks/{username}", tags=["tasks"])
async def read_user(username: str):
    return {"username": username}
