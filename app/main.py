from fastapi import FastAPI
from app.api import user, auth
from app.db.init import init_db


app = FastAPI()

app.include_router(user.router)
app.include_router(auth.router)

@app.on_event("startup")
def on_startup():
    init_db()