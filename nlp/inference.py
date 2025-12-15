from transformers import pipeline
from .config import MODEL_NAME

sentiment_pipeline = pipeline("sentiment-analysis", model = MODEL_NAME)

def predict_sentiment(text:str):
    result = sentiment_pipeline(text)[0]
    return result