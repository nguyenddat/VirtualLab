from typing import List, Optional
from pydantic import BaseModel

class Citation(BaseModel):
    """Schema for a citation with clickable URL"""
    page: int
    filename: str
    summary: str
    url: str

class CitationResponse(BaseModel):
    """Schema for citation response"""
    citations: List[Citation]
    total_count: int
    