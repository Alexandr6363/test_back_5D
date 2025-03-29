from sqlmodel import SQLModel, create_engine, Session, select
from schemas import ShortUrlApi
import uuid

sqlite_file_name = "url_short.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

engine = create_engine(sqlite_url, echo=True)


async def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


async def get_url_by_short_id(url_short_id: str):
    with Session(engine) as session:
        statement = select(ShortUrlApi).where(ShortUrlApi.id == url_short_id)
        result = session.exec(statement)
        response = result.one_or_none()
        return response


async def get_all():
    with Session(engine) as session:
        statement = select(ShortUrlApi)
        result = session.exec(statement)
        response = []
        for item in result:
            response.append(item)

        return response


async def check_short_url_id(url_short_id: str):
    with Session(engine) as session:
        statement = select(ShortUrlApi).where(ShortUrlApi.id == url_short_id)
        result = session.exec(statement)
        response = result.one_or_none()
        return True if response else False


async def get_url_by_full_url(str_url: str):
    with Session(engine) as session:
        statement = select(ShortUrlApi).where(ShortUrlApi.url == str_url)
        result = session.exec(statement)
        response = result.one_or_none()
        return response


async def generate_short_url_id():
    short_id = str(uuid.uuid4())[:10]
    is_exist = await check_short_url_id(short_id)

    if is_exist:
        generate_short_url_id()
    else:
        return short_id


async def create_url(str_url: str):
    url = await get_url_by_full_url(str_url)
    if url:
        return {
            "message": "This URL adress already exist!",
            "url": url 
        }
    else:
        new_short_url_id = await generate_short_url_id()
        with Session(engine) as session:
            new_url_pair = ShortUrlApi(id = new_short_url_id, url = str_url)
            session.add(new_url_pair)
            session.commit()
            session.refresh(new_url_pair)
            return new_url_pair 

        
 

