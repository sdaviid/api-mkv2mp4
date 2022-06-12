from sqlalchemy import(
    Column,
    Integer,
    String,
    ForeignKey
)
from sqlalchemy.types import(
    Date,
    Boolean,
    Time,
    DateTime
)
from sqlalchemy.orm import(
    relationship,
    backref
)
from app.models.base import ModelBase
from app.core.database import Base
from datetime import datetime


class File(ModelBase, Base):
    __tablename__ = "File"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    original_path = Column(String(255))
    id_status = Column(Integer, ForeignKey("FileStatus.id"))
    date_created = Column(DateTime, default=datetime.utcnow())

    @classmethod
    def add(cls, session, data):
        file = File()
        file.original_path = data.original_path
        file.id_status = 1
        session.add(file)
        session.commit()
        session.refresh(file)
        return File.find_by_id(session=session, id=file.id)


    @classmethod
    def update(cls, session, id, id_status):
        original = File.find_by_id(session, id=id)
        original.id_status = id_status
        session.commit()
        session.refresh(original)
        return original


    @classmethod
    def find_by_id_status(cls, session, id_status):
        return session.query(
            cls.id,
            cls.original_path,
            cls.id_status,
            cls.date_created
        ).filter_by(id_status=id_status).all()



class FileStatus(ModelBase, Base):
    __tablename__ = 'FileStatus'
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    description = Column(String(255))




class FileData(ModelBase, Base):
    __tablename__ = 'FileData'
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    id_file = Column(Integer)
    quality = Column(String(255))
    language = Column(String(255))
    name = Column(String(255))
    date_created = Column(DateTime, default=datetime.utcnow())


    @classmethod
    def add(cls, session, id_file, quality, language, name):
        file_data = FileData()
        file_data.id_file = data.id_file
        file_data.quality = data.quality
        file_data.language = data.language
        file_data.name = data.name
        session.add(file_data)
        session.commit()
        session.refresh(file_data)
        return FileData.find_by_id(session=session, id=file_data.id)