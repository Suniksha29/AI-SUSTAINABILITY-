# 🚀 Deployment Guide for AI Sustainability Project

## Quick Deploy Options

### Option 1: Vercel (Frontend-Focused) ⚡
**Best for:** Streamlit frontend only  
**Limitations:** 10MB bundle size, 60s timeout (not ideal for ML models)

#### Deploy Backend to Vercel:
```bash
cd "c:\Users\Lenovo\Documents\Aicte Sustainibility"
vercel --prod
```

**After deployment:**
- Update `.streamlit/secrets.toml` with your Vercel URL
- Note: TensorFlow may exceed bundle size limits

---

### Option 2: Render (Recommended for ML) ✅
**Best for:** Full-stack ML applications with TensorFlow

#### Deploy Backend to Render:
1. Go to [render.com](https://render.com) and sign up/login
2. Click **"New +"** → **"Blueprint"**
3. Connect your GitHub repository
4. Select `render.yaml` configuration
5. Click **"Apply"**

**Or manually:**
1. Create new **Web Service**
2. Connect repo: `Suniksha29/AI-SUSTAINABILITY-`
3. Build command: `pip install -r requirements.txt`
4. Start command: `uvicorn backend.app:app --host 0.0.0.0 --port $PORT`
5. Environment variable: `PORT=8000`

#### Deploy Frontend to Vercel:
1. Update `.streamlit/secrets.toml`:
   ```toml
   backend_url = "https://ai-sustainability-backend.onrender.com"
   ```
2. Push changes to GitHub
3. Deploy to Vercel (frontend only)

---

### Option 3: Railway (Easiest ML Deployment) 🎯
**Best for:** One-click ML deployments

#### Steps:
1. Go to [railway.app](https://railway.app)
2. Click **"New Project"** → **"Deploy from GitHub"**
3. Select your repository
4. Railway auto-detects Python and deploys
5. Add environment variable: `PORT=8000`

**Advantages:**
- No configuration files needed
- Larger file size limits (500MB)
- Longer timeouts (15 minutes)
- Free tier available

---

### Option 4: Hugging Face Spaces (ML-Optimized) 🤗
**Best for:** ML model demos and prototypes

#### Steps:
1. Create space at [huggingface.co/spaces](https://huggingface.co/spaces)
2. Choose **Gradio** or **Docker** SDK
3. Clone the space repository
4. Copy your files to the space
5. Push to Hugging Face

---

## Configuration Files Included

### `vercel.json`
- Serverless function configuration
- 60-second timeout setting
- Optimized Python settings

### `render.yaml`
- Complete Render deployment config
- Includes disk storage for model caching
- Auto-scaling configuration

### `api.py`
- Vercel-compatible API endpoint
- Serverless-ready FastAPI app

### `requirements-vercel.txt`
- Lightweight dependencies (no TensorFlow)
- Use this if deploying backend elsewhere

---

## Troubleshooting

### ❌ "Bundle size exceeded" on Vercel
**Solution:** Deploy backend to Render/Railway, frontend to Vercel

### ❌ "Function timeout" errors
**Solution:** 
- Use Render/Railway (longer timeouts)
- Optimize model (quantization, smaller architecture)
- Upgrade to Vercel Pro plan

### ❌ Model loading too slow
**Solution:**
- Enable model caching (Render config included)
- Use CDN for model files
- Pre-warm functions (Pro feature on most platforms)

---

## Post-Deployment Checklist

✅ **Backend API:**
- Test `/predict` endpoint with sample image
- Verify CORS settings allow frontend domain
- Check response times (< 10s ideal)

✅ **Frontend (Streamlit):**
- Update `.streamlit/secrets.toml` with backend URL
- Test image upload and classification
- Verify all features work

✅ **Monitoring:**
- Set up error logging
- Monitor API response times
- Track usage and bandwidth

---

## Cost Comparison

| Platform | Free Tier | Paid Plans | Best For |
|----------|-----------|------------|----------|
| **Vercel** | ✅ Yes (100GB/mo) | $20/mo | Frontend only |
| **Render** | ✅ Yes (750 hrs/mo) | $7/mo | Full-stack ML |
| **Railway** | ✅ Yes ($5 credit) | $5/mo | Easy ML deployment |
| **Hugging Face** | ✅ Yes | Custom | ML demos |

---

## Recommended Setup

**For Production:**
- Backend: **Render** or **Railway**
- Frontend: **Vercel**
- Total cost: ~$7-12/month

**For Development/Testing:**
- Everything on **Railway** (simplest)
- Or local development with ngrok tunneling

**For ML Model Demos:**
- **Hugging Face Spaces** (free, ML-focused audience)

---

## Need Help?

- Vercel Docs: https://vercel.com/docs
- Render Docs: https://render.com/docs
- Railway Docs: https://docs.railway.app
- Project Issues: https://github.com/Suniksha29/AI-SUSTAINABILITY-/issues
