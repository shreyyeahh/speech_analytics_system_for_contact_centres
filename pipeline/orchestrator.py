import uuid
import time

from asr.service import asr_service
from nlp.inference import predict_sentiment
from emotion.inference.emotion_inference import predict_emotion
from decision_engine.escalation_logic import should_escalate

def analyze_call(audio_path: str):
    """
    End-to-end orchestration:
    ASR → Sentiment
    Audio → Emotion
    → Decision Engine
    """
    call_id = str(uuid.uuid4())
    start_time = time.perf_counter()

    # 1 ASR Service
    asr_result = asr_service(call_id, audio_path)
    transcript = asr_result["transcript"]

    # 2 Sentiment Analysis
    sentiment_result = predict_sentiment(transcript)
    sentiment_label = sentiment_result["label"]
    sentiment_conf = float(sentiment_result["score"])

    # 3 Emotion Detection
    emotion_result = predict_emotion(audio_path)
    emotion_label = emotion_result["emotion"]
    emotion_conf = float(emotion_result["confidence"])

    # 4 Decision Engine
    escalation_decision = should_escalate(
    sentiment = sentiment_label,
    emotion = emotion_label,
    sentiment_conf = sentiment_conf,
    emotion_conf = emotion_conf
    )

    total_time = time.perf_counter() - start_time
    return {
        "call_id": call_id,
        "transcript": transcript,
        "sentiment": {
            "label": sentiment_label,
            "confidence": sentiment_conf
        },
        "emotion": {
            "label": emotion_label,
            "confidence": emotion_conf
        },
        "escalation": escalation_decision,
        "processing_time_sec": total_time
    }



