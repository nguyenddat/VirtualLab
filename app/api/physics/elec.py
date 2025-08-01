from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse

from schemas.physics.elec import ElecRequest

from utils.chatbot_utils.state import State
from services.physic_explain import explain_physics

router = APIRouter()

@router.post("/elec/explain")
async def explain_electricity_concept(request: ElecRequest):
    """
    Endpoint to explain a concept in electricity.
    
    :param request: ElecRequest containing the concept to explain.
    :return: JSON response with the explanation.
    """
    new_state = State(graph=str(request.graph), question=request.question, data=[])
    response_state = explain_physics(new_state)
    return JSONResponse(content={
        "response": response_state.response
    })
