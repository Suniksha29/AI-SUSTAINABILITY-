# AI-Powered Waste Segregation & Recycling Recommendation System

Minimal prototype to classify waste images and provide recycling/disposal recommendations.

Contents
- `backend/` - FastAPI app and model wrapper
- `model/` - where trained model is saved (not included)
- `scripts/train.py` - training script using MobileNetV2 (transfer learning)
- `streamlit_app.py` - simple UI to upload image and show prediction
- `requirements.txt` - Python dependencies
- `tests/` - small unit test(s)

Quick start (Windows / PowerShell):

1) Create and activate a virtual env

```powershell
python -m venv .venv; .\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

2) Start backend

```powershell
python backend/app.py
# or: uvicorn backend.app:app --host 0.0.0.0 --port 8000 --reload
```

3) Start frontend (Streamlit)

```powershell
streamlit run streamlit_app.py
```

Notes:
- The repository includes a classifier wrapper that will load `model/model.h5` if present. If there's no model file, the API returns a mock/deterministic prediction to allow development without a trained model.
- Training requires the TrashNet dataset (or similar) and a GPU for reasonable speed; see `scripts/train.py`.

License: MIT
