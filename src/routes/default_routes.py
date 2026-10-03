from fastapi import APIRouter

from src.models import IndexResponseModel

router = APIRouter(tags=["default"])


@router.get("/", response_model=IndexResponseModel)
def index_route():
    return {"data": {"message": "Index route reached"}}


@router.get("/about", response_model=IndexResponseModel)
async def about_route():
    return {"data": {"message": "About page"}}
