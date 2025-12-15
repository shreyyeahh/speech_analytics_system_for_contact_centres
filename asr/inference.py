import whisper
from .config import MODEL_SIZE, LANGUAGE
model = whisper.load_model(MODEL_SIZE)


def transcribe(audio_path):
    result = model.transcribe(audio_path, language = LANGUAGE)
    return result["text"]
