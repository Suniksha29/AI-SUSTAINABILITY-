from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import os
import sys

# Add parent directory to Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from backend.model import WasteClassifier, RECOMMENDATIONS
import uvicorn

app = FastAPI(title="Waste Segregation API")

app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])

classifier = WasteClassifier()


class PredictResponse(BaseModel):
    category: str
    confidence: float
    recommendation: str


@app.post("/predict", response_model=PredictResponse)
async def predict(file: UploadFile = File(...)):
    """Accepts an image file and returns category, confidence and recommendation."""
    contents = await file.read()
    category, confidence = classifier.predict_image_bytes(contents)
    recommendation = RECOMMENDATIONS.get(category, "Dispose according to local rules.")
    return PredictResponse(category=category, confidence=float(confidence), recommendation=recommendation)


if __name__ == "__main__":
    # Run with: python backend/app.py
    uvicorn.run("backend.app:app", host="0.0.0.0", port=8000, reload=True)
