from dotenv import load_dotenv
load_dotenv()

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from starlette.middleware.cors import CORSMiddleware

from app.core.config import config

from app.api import electric_explain_router, student_explain_router

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
    return app

app = get_application()