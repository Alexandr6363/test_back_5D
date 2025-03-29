from sqlmodel import SQLModel, Field



class ShortUrlApi(SQLModel, table=True):
    id: str | None = Field(default=None, primary_key=True)
    url: str