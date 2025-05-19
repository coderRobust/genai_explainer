from fastapi import FastAPI, HTTPException
from app.models import ExplanationRequest, ExplanationResponse
import asyncio
import logging

app = FastAPI(title="GenAI Explainer Service")


@app.get("/health")
async def health():
    """
    Health check endpoint.
    Returns 200 OK to confirm the server is running.
    """
    return {"status": "ok"}


async def get_mock_explanation(concept: str, audience: str) -> str:
    """
    Simulates a delay from an LLM and returns a hardcoded explanation.
    """
    await asyncio.sleep(1)  # Simulate LLM latency
    return (
        f"Okay, imagine explaining '{concept}' to a '{audience}'. "
        f"It's basically a simplified idea that helps make {concept} easier to understand."
    )


@app.post("/explain", response_model=ExplanationResponse)
async def explain_concept(request: ExplanationRequest):
    """
    Accepts a concept and target audience, and returns a simplified explanation.
    Simulates a delayed response as if it came from an LLM.
    """
    if not request.concept.strip():
        raise HTTPException(
            status_code=400, detail="Concept must not be empty")
    if not request.audience.strip():
        raise HTTPException(
            status_code=400, detail="Audience must not be empty")

    try:
        explanation = await get_mock_explanation(request.concept, request.audience)
        return ExplanationResponse(
            concept=request.concept,
            audience=request.audience,
            explanation=explanation
        )
    except Exception as e:
        logging.error("Error generating explanation", exc_info=True)
        raise HTTPException(status_code=500, detail="Internal server error")
