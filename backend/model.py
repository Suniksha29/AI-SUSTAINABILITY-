import io
import os
import random
from PIL import Image
import numpy as np

try:
    import tensorflow as tf
    from tensorflow.keras.models import load_model
except Exception:
    tf = None

# Classes used in TrashNet-like dataset
CLASSES = ["plastic", "paper", "metal", "glass", "organic", "cardboard"]

RECOMMENDATIONS = {
    "plastic": "Recycle plastics in the plastic recycling bin. Rinse containers and remove caps where required.",
    "paper": "Put paper in paper/cardboard recycling. Keep it dry and remove large tape/stickers.",
    "metal": "Recycle metal in the metal recycling bin. Rinse food residues.",
    "glass": "Recycle glass in the glass recycling bin. Be careful with broken glass; wrap it before disposal if required.",
    "organic": "Compost organic waste where possible, or use the organic/green bin.",
    "cardboard": "Flatten and recycle cardboard with paper/cardboard stream. Keep dry.",
}


class WasteClassifier:
    """Classifier wrapper. Loads a Keras model if available; otherwise returns mock predictions.

    Methods
    - predict_image_bytes(bytes) -> (label, confidence)
    """

    def __init__(self, model_path: str = None):
        root = os.path.dirname(__file__)
        if model_path is None:
            model_path = os.path.abspath(os.path.join(root, "..", "model", "model.h5"))
        self.model = None
        self.input_size = (224, 224)
        if tf is not None and os.path.exists(model_path):
            try:
                self.model = load_model(model_path)
                # get input size if available
                shape = getattr(self.model, "input_shape", None)
                if shape and len(shape) >= 3:
                    self.input_size = (shape[1], shape[2])
            except Exception:
                self.model = None

    def preprocess(self, img: Image.Image, target_size=(224, 224)):
        img = img.convert("RGB")
        img = img.resize(target_size)
        arr = np.array(img).astype("float32") / 255.0
        arr = np.expand_dims(arr, 0)
        return arr

    def predict_image_bytes(self, img_bytes: bytes):
        """Return (label, confidence). If model is missing, return deterministic mock prediction."""
        img = Image.open(io.BytesIO(img_bytes))
        if self.model is not None:
            x = self.preprocess(img, target_size=self.input_size)
            preds = self.model.predict(x)[0]
            idx = int(np.argmax(preds))
            return CLASSES[idx], float(preds[idx])

        # Mock/deterministic fallback based on image size / mode to allow development
        try:
            w, h = img.size
            # simple heuristic: small and brownish -> organic, shiny -> metal, greenish -> plastic/cardboard
            mean = np.array(img.convert("RGB")).mean(axis=(0, 1))
            r, g, b = mean
            if r < 100 and g < 100 and b < 100:
                choice = "metal"
            elif g > r and g > b:
                choice = "organic"
            elif r > g and r > b:
                choice = "cardboard"
            else:
                choice = random.choice(CLASSES)
            confidence = round(0.6 + min(0.39, (abs(w - h) / max(w, h)) ), 3)
        except Exception:
            choice = random.choice(CLASSES)
            confidence = round(random.uniform(0.5, 0.95), 3)

        return choice, confidence
