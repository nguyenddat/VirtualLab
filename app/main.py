from dotenv import load_dotenv
load_dotenv()

from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from api.physics.elec import router as elec_router
from api.physics.create_tool import router as create_tool_router
from api.education.tutor import router as tutor_router
from api.education.teacher_assistant import router as teacher_router
from api.education.tool_generator import router as tool_router

def get_application() -> FastAPI:
    app = FastAPI(
        title="VirtualLab - Educational AI Services",
        description="API cho các dịch vụ AI giáo dục: AI gia sư, AI hỗ trợ giáo viên, AI tạo sinh dụng cụ",
        version="1.0.0"
    )
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    """Register API routers."""
    app.include_router(elec_router, prefix="/api/physics", tags=["physics"])
    app.include_router(create_tool_router, prefix="/api/physics", tags=["physics"])
    app.include_router(tutor_router, prefix="/api/education", tags=["education"])
    app.include_router(teacher_router, prefix="/api/education", tags=["education"])
    app.include_router(tool_router, prefix="/api/education", tags=["education"])
    return app

app = get_application()
# if __name__ == "__main__":
#     uvicorn.run(app, host="localhost", port=8000, log_level="info", reload=True)