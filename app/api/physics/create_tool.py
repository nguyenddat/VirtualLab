from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse

from app.schemas.physics.elec import ElecRequest

from app.services.create_tool import create_tool

router = APIRouter()

from pydantic import BaseModel
class CreateToolRequest(BaseModel):
    question: str


@router.post("/elec/create_tool")
async def create_tool_api(request: CreateToolRequest):
    """
    Endpoint to explain a concept in electricity.
    
    :param request: ElecRequest containing the concept to explain.
    :return: JSON response with the explanation.
    """
    question = request.question
    create_tool(params = {"question": question})
    return JSONResponse(content={
        "response": 200
    })
