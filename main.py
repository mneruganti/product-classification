from fastapi import FastAPI
from pydantic import BaseModel
from sentence_transformers import SentenceTransformer
import joblib
import logging

# ✅ Set up logging
logging.basicConfig(
    filename="api_logs.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Load models
sbert = SentenceTransformer("all-MiniLM-L6-v2")
clf = joblib.load("rf_model.pkl")

app = FastAPI()

class Product(BaseModel):
    title: str

@app.get("/")
def read_root():
    return {"message": "Product Category Classification API"}

@app.post("/predict")
def predict_category(product: Product):
    embedding = sbert.encode([product.title])
    prediction = clf.predict(embedding)[0]
    
    # ✅ Log the input and prediction
    logging.info(f"Received: '{product.title}' → Predicted Category: {prediction}")

    return {
        "title": product.title,
        "predicted_category_id": int(prediction)
    }
