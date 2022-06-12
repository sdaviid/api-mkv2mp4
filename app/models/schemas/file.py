from datetime import date
from pydantic import Field
from datetime import datetime
from pydantic import BaseModel



class baseSchema(BaseModel):
    class Config:
        orm_mode = True


class FileAdd(baseSchema):
    original_path: str = Field(title="Original URL")
    


class FileDetail(baseSchema):
    id: int
    original_path: str
    id_status: int
    date_created: datetime


class FileStatusUpdate(baseSchema):
    id_status: int


class FileAddData(baseSchema):
    id_file: int
    quality: str
    language: str
    name: str
