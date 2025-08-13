from pydantic import BaseModel

class CreateSubjectRequest(BaseModel):
    name: str
    description: str | None = None