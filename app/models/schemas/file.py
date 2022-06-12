from datetime import date
from pydantic import Field
from datetime import datetime
from pydantic import BaseModel




class FileAdd(BaseModel):
    original_path: str = Field(title="Original URL")
    class Config:
        orm_mode = True


class FileDetail(BaseModel):
    id: int
    original_path: str
    id_status: int
    date_created: datetime
    class Config:
        orm_mode = True


class FileStatusUpdate(BaseModel):
    id_status: int