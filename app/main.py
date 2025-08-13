from dotenv import load_dotenv
load_dotenv()

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from starlette.middleware.cors import CORSMiddleware

from database.init_db import get_db

from api import electric_explain_router, student_explain_router, subject_router, bookset_router, book_router, chapter_router, experiment_router

def get_application() -> FastAPI:
    app = FastAPI()
    app.mount("/static", StaticFiles(directory="static"), name="static")
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    """Register API routers."""
    app.include_router(electric_explain_router, prefix="/api/physics", tags=["physics"])
    app.include_router(student_explain_router, prefix="/api/physics", tags=["physics"])
    app.include_router(subject_router, prefix="/api/subject", tags=["subject"])
    app.include_router(bookset_router, prefix="/api/bookset", tags=["bookset"])
    app.include_router(chapter_router, prefix="/api/chapter", tags=["chapter"])
    app.include_router(experiment_router, prefix="/api/experiment", tags=["experiment"])
    app.include_router(book_router, prefix="/api/book", tags=["book"])
    return app

app = get_application()