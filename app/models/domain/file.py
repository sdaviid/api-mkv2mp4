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
from utils.utils import md5


class File(ModelBase, Base):
    __tablename__ = "File"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    original_path = Column(String(255))
    md5_name = Column(String(255))
    md5_father = Column(String(255), default=None)
    id_status = Column(Integer, ForeignKey("FileStatus.id"))
    date_created = Column(DateTime, default=datetime.utcnow())

    @classmethod
    def add(cls, session, data):
        file = File()
        file.original_path = data.original_path
        file.md5_name = md5(data.original_path[data.original_path.rindex('/')+1:])
        file.md5_father = data.md5_father
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
            cls.md5_name,
            cls.md5_father,
            cls.id_status,
            cls.date_created
        ).filter_by(id_status=id_status).all()


    @classmethod
    def find_by_hash(cls, session, md5_name):
        return session.query(
            cls.id,
            cls.original_path,
            cls.md5_name,
            cls.md5_father,
            cls.id_status,
            cls.date_created
        ).filter_by(md5_name=md5_name).first()


    @classmethod
    def find_by_md5_father(cls, session, md5_father):
        return session.query(
            cls.id,
            cls.original_path,
            cls.md5_name,
            cls.md5_father,
            cls.id_status,
            cls.date_created
        ).filter_by(md5_father=md5_father).all()



class FileStatus(ModelBase, Base):
    __tablename__ = 'FileStatus'
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    description = Column(String(255))




class FileData(ModelBase, Base):
    __tablename__ = 'FileData'
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    id_file = Column(Integer)
    md5_name = Column(String(255))
    md5_father = Column(String(255), default=None)
    quality = Column(String(255))
    language = Column(String(255))
    name = Column(String(255))
    date_created = Column(DateTime, default=datetime.utcnow())


    @classmethod
    def add(cls, session, id_file, md5_name, quality, language, name, md5_father=None):
        file_data = FileData()
        file_data.id_file = id_file
        file_data.md5_name = md5_name
        file_data.md5_father = md5_father
        file_data.quality = quality
        file_data.language = language
        file_data.name = name
        session.add(file_data)
        session.commit()
        session.refresh(file_data)
        return FileData.find_by_id(session=session, id=file_data.id)



    @classmethod
    def find_by_id_file(cls, session, id_file):
        return session.query(
            cls.id,
            cls.id_file,
            cls.md5_name,
            cls.md5_father,
            cls.quality,
            cls.language,
            cls.name,
            cls.date_created
        ).filter_by(id_file=id_file).all()



    @classmethod
    def find_by_md5(cls, session, md5_name):
        return session.query(
            cls.id,
            cls.id_file,
            cls.md5_name,
            cls.md5_father,
            cls.quality,
            cls.language,
            cls.name,
            cls.date_created
        ).filter_by(md5_name=md5_name).all()


    @classmethod
    def find_by_md5_father(cls, session, md5_father):
        return session.query(
            cls.id,
            cls.id_file,
            cls.md5_name,
            cls.md5_father,
            cls.quality,
            cls.language,
            cls.name,
            cls.date_created
        ).filter_by(md5_father=md5_father).all()