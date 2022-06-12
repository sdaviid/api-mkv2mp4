from typing import List
from sqlalchemy.orm import Session
from fastapi import(
    Depends,
    Response,
    status,
    APIRouter
)
from fastapi.responses import JSONResponse


from app.models.domain.file import(
    File,
    FileStatus,
    FileData

)
from app.models.schemas.file import(
    FileAdd,
    FileDetail,
    FileStatusUpdate
)


from app.core.database import get_db


router = APIRouter()


@router.post(
    '/add',
    status_code=status.HTTP_200_OK,
    response_model=FileDetail
)
def add_file(data: FileAdd, response: Response, db: Session = Depends(get_db)):
    """List all logs"""
    return File.add(session=db, data=data)


@router.get(
    '/status/{id}',
    status_code=status.HTTP_200_OK,
    response_model=FileDetail
)
def add_file(id: int, response: Response, db: Session = Depends(get_db)):
    """List all logs"""
    return File.find_by_id(session=db, id=id)



@router.put(
    '/update/{id}',
    status_code=status.HTTP_200_OK,
    response_model=FileDetail
)
def add_file(id: int, data: FileStatusUpdate, response: Response, db: Session = Depends(get_db)):
    """List all logs"""
    return File.update(session=db, id=id, data=data)