import streamlit as st
import requests
from PIL import Image
import io

BACKEND_URL = st.secrets.get("backend_url", "http://localhost:8000")

st.set_page_config(page_title="Waste Segregation Assistant", layout="centered")
st.title("AI Waste Segregation & Recycling Assistant")

st.write("Upload an image of a waste item and get a classification and recycling recommendation.")

uploaded = st.file_uploader("Choose an image", type=["jpg", "jpeg", "png"])

if uploaded is not None:
    img = Image.open(uploaded)
    st.image(img, caption="Uploaded image", use_column_width=True)

    if st.button("Classify"):
        with st.spinner("Sending to backend..."):
            try:
                files = {"file": (uploaded.name, uploaded.getvalue(), uploaded.type)}
                resp = requests.post(f"{BACKEND_URL}/predict", files=files, timeout=15)
                resp.raise_for_status()
                data = resp.json()
                st.success(f"Predicted: {data['category']} (confidence: {data['confidence']:.2f})")
                st.info(data.get("recommendation", "Follow local disposal rules."))
                # Add sustainability tip
                tips = {
                    "plastic": "Reduce single-use plastics; recycle when possible.",
                    "paper": "Reuse paper, and recycle to save trees and energy.",
                    "metal": "Recycling metals saves a lot of energy vs new production.",
                    "glass": "Glass is highly recyclable — prefer reuse where possible.",
                    "organic": "Composting organic waste reduces methane emissions.",
                    "cardboard": "Flatten cardboard to save transport volume when recycling.",
                }
                tip = tips.get(data.get("category"), "Follow local recycling guidelines.")
                st.write("### Sustainability tip")
                st.write(tip)
            except Exception as e:
                st.error(f"Error calling backend: {e}")
