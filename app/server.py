from fastapi import FastAPI
from .db import  create_db_and_tables
from .router import router as url_router


create_db_and_tables()

app = FastAPI()
app.include_router(url_router)


