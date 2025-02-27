from fastapi import APIRouter, Request
from src.config import templates

router = APIRouter()

@router.get("/")
async def index(request: Request):
    return templates.TemplateResponse("main.html", {"request": request})