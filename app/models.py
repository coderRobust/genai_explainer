from pydantic import BaseModel, Field


class ExplanationRequest(BaseModel):
    concept: str = Field(..., min_length=1,
                         description="The concept to explain")
    audience: str = Field(..., min_length=1, description="The target audience")


class ExplanationResponse(BaseModel):
    concept: str
    audience: str
    explanation: str
