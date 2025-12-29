from fastapi import APIRouter
from app.schemas.echo import EchoRequest

router = APIRouter()

@router.post("/echo")
def echo(req: EchoRequest):
    return {"echo": req.message}