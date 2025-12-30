from fastapi import FastAPI
from app.api import user
from app.db.init import init_db


app = FastAPI()

app.include_router(user.router)

@app.on_event("startup")
def on_startup():
    init_db()