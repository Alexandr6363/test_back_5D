from sqlmodel import SQLModel, Field



class ShortUrlApi(SQLModel, table=True):
    id: str = Field(primary_key=True)
    url: str