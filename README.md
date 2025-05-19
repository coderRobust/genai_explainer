# GenAI Explainer Service

## 🧠 Overview
A FastAPI-based microservice that simulates an LLM-powered assistant to explain complex technical concepts to non-technical audiences. This version simulates latency and returns mock explanations.

## 🚀 Requirements
- Python 3.10

## 🛠️ Local Setup
```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

## 🐳 Docker Setup
```bash
docker build -t genai_explainer .
docker run -p 8000:8000 genai_explainer
```

## 🔌 API Endpoints
### ✅ GET `/health`
Returns a health status.
```json
{ "status": "ok" }
```

### ✅ POST `/explain`
Returns a simulated LLM explanation.
```json
Request:
{
  "concept": "Quantum Computing",
  "audience": "5-year-old"
}
Response:
{
  "concept": "Quantum Computing",
  "audience": "5-year-old",
  "explanation": "Okay, imagine explaining 'Quantum Computing' to a '5-year-old'. It's basically a simplified idea that helps make Quantum Computing easier to understand."
}
```

## 🧪 Run Tests
```bash
pytest
```