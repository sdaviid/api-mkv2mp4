from fastapi import(
    Depends,
    FastAPI,
    HTTPException,
    Response,
    status
)
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from starlette.responses import RedirectResponse


from app.core.database import(
    SessionLocal,
    engine,
    Base
)

from app.api.base import api_router
from app.watch.watcher import watcher


Base.metadata.create_all(bind=engine)

OUTPUT_PATH_FFMPEG_FILES = '/var/www/html/'
inst_watcher = watcher(SessionLocal(), OUTPUT_PATH_FFMPEG_FILES)
inst_watcher.start()


app = FastAPI(
    title="ffmpeg MKV to MP4"
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)



app.include_router(api_router)