from dotenv import load_dotenv
load_dotenv()

from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from app.api.physics.elec import router as elec_router

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
    app.include_router(elec_router, prefix="/api/physics", tags=["physics"])
    return app

app = get_application()
# if __name__ == "__main__":
#     uvicorn.run(app, host="localhost", port=8000, log_level="info", reload=True)