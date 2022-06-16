from datetime import date
from pydantic import Field
from datetime import datetime
from pydantic import BaseModel
from typing import Optional


class baseSchema(BaseModel):
    class Config:
        orm_mode = True


class FileAdd(baseSchema):
    original_path: str = Field(title="Original URL")
    md5_father: Optional[str] = None
    


class FileDetail(baseSchema):
    id: int
    original_path: str
    md5_name: str
    md5_father: Optional[str] = None
    id_status: int
    date_created: datetime


class FileStatusUpdate(baseSchema):
    id_status: int


class FileAddData(baseSchema):
    id_file: int
    md5_name: str
    md5_father: Optional[str] = None
    quality: str
    language: str
    name: str
