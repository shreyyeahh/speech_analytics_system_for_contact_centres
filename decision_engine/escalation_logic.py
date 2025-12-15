def should_escalate(sentiment: str, emotion : str, sentiment_conf : float, emotion_conf : float):
    reasons = []

    if sentiment == "negative" and sentiment_conf > 0.7:
        reasons.append("Strong negative sentiment")

    if emotion in ["angry", "fearful"] and emotion_conf > 0.6:
        reasons.append(f"Detected high- risk emotion: {emotion}")

    if sentiment_conf < 0.5 or emotion_conf < 0.5:
        reasons.append("low confidence signals")

    escalate = len(reasons) > 0

    return {
        "escalate": escalate,
        "reasons" : reasons
    }             