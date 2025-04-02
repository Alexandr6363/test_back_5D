from fastapi import APIRouter
from .services import create_url, get_all_url, get_url_by_short_id
from fastapi.responses import RedirectResponse


router = APIRouter(
   prefix="",
   tags=["Short url"],
)


@router.post("/", status_code=201)
async def create_shortened_url(str_url: str):
    await create_url(str_url)


@router.get("/urls_list")
async def get_list_of_url():
    result = await get_all_url()
    if result:
        return result
    else:
        return {"error": "URLs not found"}   


@router.get("/", status_code=307)
async def redirect_to_original(short_id: str):
    url = await get_url_by_short_id(short_id)
    if url:
        response = RedirectResponse(url=url.url)
        response.headers["Location"] = url.url
        return response
    else:
        return {"error": "URL not found"}
