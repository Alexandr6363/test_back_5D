from fastapi import FastAPI
from services import create_url, get_url_by_short_id, create_db_and_tables
from fastapi.responses import RedirectResponse


app = FastAPI()

@app.post("/", status_code=201)
async def create_shortened_url(str_url: str):
    create_url(str_url)

@app.get("/{short_id}")
async def redirect_to_original(short_id: str):
    url = get_url_by_short_id(short_id)
    if url:
        response = RedirectResponse(
            url=url,
            status_code=307
        )
        response.headers["Location"] = url
        return response
    else:
        return {"error": "URL not found"}

if __name__ == "__main__":
    create_db_and_tables()
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8080)