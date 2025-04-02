from sqlmodel import select
from .schemas import ShortUrlApi
import uuid
from .db import async_engine as engine
from sqlalchemy.ext.asyncio import AsyncSession


async def get_url_by_short_id(url_short_id: str):
    async with AsyncSession(engine) as session:
        statement = select(ShortUrlApi).where(ShortUrlApi.id == url_short_id)
        result = await session.execute(statement)
        response = result.scalar_one_or_none()
        return response


async def get_all_url():
    async with AsyncSession(engine) as session:
        statement = select(ShortUrlApi)
        result = await session.execute(statement)
        response = result.scalars().all()
        return response


async def check_short_url_id(url_short_id: str):
    async with AsyncSession(engine) as session:
        statement = select(ShortUrlApi).where(ShortUrlApi.id == url_short_id)
        result = await session.execute(statement)
        response = result.scalar_one_or_none()
        return True if response else False


async def get_url_by_full_url(str_url: str):
    async with AsyncSession(engine) as session:
        statement = select(ShortUrlApi).where(ShortUrlApi.url == str_url)
        result = await session.execute(statement)
        response = result.scalar_one_or_none()
        return response


async def generate_short_url_id():
    short_id = str(uuid.uuid4())[:5]
    is_exist = await check_short_url_id(short_id)

    if is_exist:
        return await generate_short_url_id()
    else:
        return short_id


async def create_url(str_url: str):
    str_url = check_full_url(str_url)
    url = await get_url_by_full_url(str_url)
    if url:
        return {
            "message": "This URL adress already exist!",
            "url": url 
        }
    else:
        new_short_url_id = await generate_short_url_id()
        async with AsyncSession(engine) as session:
            new_url_pair = ShortUrlApi(id = new_short_url_id, url = str_url)
            session.add(new_url_pair)
            await session.commit()
            await session.refresh(new_url_pair)
            return new_url_pair 
        

def check_full_url(url):
    if url.startswith("https://") or url.startswith("http://"):
        return url
    else:
        return f"https://{url}"

        
 

