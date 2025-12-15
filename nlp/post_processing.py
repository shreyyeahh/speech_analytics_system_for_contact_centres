from .config import CONFIDENCE_THRESHOLD

def normalize_output(model_output):
    label = model_output["label"].lower()
    score = model_output["score"]

    if score < CONFIDENCE_THRESHOLD:
        
        return {
            "sentiment":"neutral",
            "confidence":score
        }
    return{
        "sentiment":label,
        "confidence":score
    }