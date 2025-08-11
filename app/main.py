from dotenv import load_dotenv
load_dotenv()

from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from core.config import config
# from fastapi_sqlalchemy import DBSessionMiddleware
# from database import init_db  # Import để khởi tạo database
    # app.add_middleware(DBSessionMiddleware, db_url=config.database_url)

from api import electric_explain_router

def get_application() -> FastAPI:
    app = FastAPI()

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    """Register API routers."""
    app.include_router(electric_explain_router, prefix="/api/physics", tags=["physics"])
    # app.include_router(experiment_router, prefix="/api/experiment", tags=["experiment"])
    return app

app = get_application()