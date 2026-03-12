# Vercel Deployment Instructions

## Important Notes

⚠️ **Vercel Limitations for this Project:**
- Vercel has a **10MB limit** on serverless function bundles
- TensorFlow models are typically **large** (can exceed 100MB)
- Cold starts can be **slow** (30+ seconds) for ML models
- **Timeout limits**: Serverless functions timeout after 10s (Hobby plan) or 60s (Pro plan)

## Alternative Recommendations

For ML/AI projects like this, consider these platforms instead:

1. **Render** (render.com) - Better for FastAPI + ML models
2. **Railway** (railway.app) - Great for full-stack apps with ML
3. **Hugging Face Spaces** - Optimized for ML models
4. **Google Cloud Run** or **AWS Lambda** with larger limits

## Deploy to Vercel Anyway (if model is small enough)

### Step 1: Install Vercel CLI
```bash
npm install -g vercel
```

### Step 2: Login to Vercel
```bash
vercel login
```

### Step 3: Deploy
```bash
vercel --prod
```

### Step 4: Update Streamlit Backend URL
After deployment, update the backend URL in your Streamlit app:
- Go to `.streamlit/secrets.toml`
- Set `backend_url = "https://your-deployment-url.vercel.app"`

## Local Testing of Vercel Functions

```bash
# Install Vercel CLI
npm install -g vercel

# Test locally
vercel dev
```

## Troubleshooting

### Model Too Large
If you get "bundle size exceeded" error:
1. Use a smaller model (MobileNet, etc.)
2. Host model separately (Google Drive, AWS S3)
3. Load model from URL at runtime

### Timeout Issues
ML inference can be slow. Consider:
1. Optimize model (quantization, pruning)
2. Use Vercel Pro plan for longer timeouts
3. Switch to platforms with better ML support

### Alternative: Deploy Frontend Only to Vercel

Deploy only the Streamlit frontend to Vercel and host backend elsewhere:

1. **Backend**: Deploy to Render/Railway/Heroku
2. **Frontend**: Deploy to Vercel

Update `.streamlit/secrets.toml`:
```toml
backend_url = "https://your-backend-url.onrender.com"
```
