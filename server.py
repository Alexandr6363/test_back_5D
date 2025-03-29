from fastapi import FastAPI
from services import create_url, get_url_by_short_id, create_db_and_tables, get_all
from fastapi.responses import RedirectResponse


app = FastAPI()

@app.post("/", status_code=201)
async def create_shortened_url(str_url: str):
    await create_url(str_url)


@app.get("/all")
async def get_all_url():
    result = await get_all()
    return result



@app.get("/", status_code=307)
async def redirect_to_original(short_id: str):
    url = await get_url_by_short_id(short_id)
    if url:
        response = RedirectResponse(url=url.url)
        response.headers["Location"] = url.url
        return response
    else:
        return {"error": "URL not found"}

if __name__ == "__main__":
    create_db_and_tables()
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8080)