# REST: resource-oriented, stateless, HTTP verbs map to CRUD.
# Run: uvicorn rest_server:app --port 8000
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()
users_by_id: dict[int, dict] = {}
next_user_id = 1


class UserPayload(BaseModel):
    name: str
    email: str


@app.post("/users", status_code=201)
def create_user(payload: UserPayload):
    global next_user_id
    user_record = {"id": next_user_id, **payload.model_dump()}
    users_by_id[next_user_id] = user_record
    next_user_id += 1
    return user_record


@app.get("/users")
def list_users():
    return list(users_by_id.values())


@app.get("/users/{user_id}")
def get_user(user_id: int):
    if user_id not in users_by_id:
        raise HTTPException(status_code=404, detail="User not found")
    return users_by_id[user_id]


@app.put("/users/{user_id}")
def update_user(user_id: int, payload: UserPayload):
    if user_id not in users_by_id:
        raise HTTPException(status_code=404, detail="User not found")
    users_by_id[user_id] = {"id": user_id, **payload.model_dump()}
    return users_by_id[user_id]


@app.delete("/users/{user_id}", status_code=204)
def delete_user(user_id: int):
    if users_by_id.pop(user_id, None) is None:
        raise HTTPException(status_code=404, detail="User not found")
