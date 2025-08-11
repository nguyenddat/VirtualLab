import json

from fastapi import APIRouter
from fastapi.responses import StreamingResponse

from schemas import ElectricExplainRequest
from utils.chatbot_utils.state import State
from services.physic_explain import explain_physics


router = APIRouter()

def generate_stream(generation):
    try:
        chunk_count = 0
        last_answer = ""
        for chunk in generation:
            chunk_count += 1
            last_answer = chunk
            response_data = {
                "type": "content",
                "chunk_id": chunk_count,
                "content": chunk,
                "status": "streaming"        
            }
            print(chunk, end="\n")
            yield f"data: {json.dumps(response_data, ensure_ascii=False)}\n\n"
        
        final_data = {
            "type": "content",
            "chunk_id": chunk_count + 1,
            "content": last_answer,
            "status": "completed"
        }
        yield f"data: {json.dumps(final_data, ensure_ascii=False)}\n\n"
    
    except Exception as e:
        error_data = {
            "type": "error",
            "error": str(e)
        }
        yield f"data: {json.dumps(error_data, ensure_ascii=False)}\n\n"
    
    finally:
        yield "event: close\ndata: {}\n\n"


@router.post("/electric_explain")
async def electric_explain(request: ElectricExplainRequest):
    state = State(
        question=request.question,
        graph=str(request.graph),
        data=[],
        response="",
        recommendations=[]
    )

    return StreamingResponse(
        generate_stream(explain_physics(state)),
        media_type="text/event-stream",
        headers={
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Headers": "Content-Type",
        },
    )