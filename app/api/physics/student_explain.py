import os
import json

from fastapi import APIRouter
from fastapi.responses import StreamingResponse

from app.schemas import ElectricExplainRequest
from app.utils.chatbot_utils.state import State
from app.services.physic_explain import explain_physics
from app.services.rag import Rag


router = APIRouter()
rag = Rag(file_name="SGK VL 11 CTST.pdf")

def generate_stream(generation):
    try:
        chunk_count = 0
        last_answer = ""
        sources = []
        for chunk in generation:
            if isinstance(chunk, dict):
                sources = chunk.get("sources", [])
                chunk = chunk.get("response", "")
            else:
                last_answer = chunk

            chunk_count += 1
            response_data = {
                "type": "content",
                "chunk_id": chunk_count,
                "content": chunk,
                "sources": sources,
                "status": "streaming"        
            }
            yield f"data: {json.dumps(response_data, ensure_ascii=False)}\n\n"
        
        final_data = {
            "type": "content",
            "chunk_id": chunk_count + 1,
            "content": last_answer,
            "sources": sources,
            "status": "completed"
        }
        print(final_data)
        yield f"data: {json.dumps(final_data, ensure_ascii=False)}\n\n"
    
    except Exception as e:
        error_data = {
            "type": "error",
            "error": str(e)
        }
        yield f"data: {json.dumps(error_data, ensure_ascii=False)}\n\n"
    
    finally:
        yield "event: close\ndata: {}\n\n"


@router.post("/student_explain")
async def student_explain(request: ElectricExplainRequest):
    state = State(
        question=request.question,
        graph=str(request.graph),
        data=[],
        response="",
        recommendations=[]
    )

    return StreamingResponse(
        generate_stream(rag.invoke(state)),
        media_type="text/event-stream",
        headers={
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Headers": "Content-Type",
        },
    )