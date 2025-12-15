from .preprocessing import clean_text
from .inference import predict_sentiment
from .post_processing import normalize_output

def sentiment_service(call_id:str, transcript:str):
    clean = clean_text(transcript)
    if not clean: # Handle empty transcript
        return {
            "call_id": call_id,
            "sentiment": "unknown",
            "confidence": 0.0
        }
    
    raw_result = predict_sentiment(clean)
    final_result = normalize_output(raw_result)

    return{
        "call_id":call_id,
        "sentiment":final_result["sentiment"],
        "confidence":final_result["confidence"]
    }
