from fastapi import FastAPI

app = FastAPI(
    title = "Game moderation"
)

Users = [
    {"id": 1 , "role": "admin", "name": "kaktuz2000"},
    {"id": 2 , "role": "moderator", "name": "BAZA"},
    {"id": 3 , "role": "moderator", "name": "Menaker"},
    {"id": 4 , "role": "user", "name": "Помидорка"},
    {"id": 5 , "role": "user", "name": "Maqio"},
    {"id": 6 , "role": "user", "name": "Lis"},
]
@app.get("/users/{user_id}")
def get_user(user_id: int):
    return [user for user in Users if user.get("id") == user_id]

Solutions = [
    {"id": 1, "user_id": 1, "product": "Escape from Tarkov", "result": "pass"},
    {"id": 2, "user_id": 3, "product": "Super meat boy", "result": "deny"},
    {"id": 3, "user_id": 3, "product": "Dota 2", "result": "pass"},
    {"id": 4, "user_id": 1, "product": "Portal", "result": "pass"},
    {"id": 5, "user_id": 2, "product": "Will To live Online", "result": "deny"},
    {"id": 6, "user_id": 1, "product": "Portal 2", "result": "pass"},
    {"id": 7, "user_id": 1, "product": "Paladins", "result": "deny"},
    {"id": 8, "user_id": 2, "product": "Elden Ring", "result": "pass"},
]

@app.get("/solutions")
def get_solutions(limit: int = 5, offset: int = 0):
    return Solutions[offset:][:limit]

@app.post("/users/{user_id}")
def change_user_role(user_id: int, new_role: str):
    current_user = list(filter(lambda user: user.get("id") == user_id, Users))[0]
    current_user["role"] = new_role
    return {"data": current_user}