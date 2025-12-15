from .loader import load_audio
from .inference import transcribe
from .postprocessing import clean_text

def asr_service(call_id,audio_path):
    audio = load_audio(audio_path)
    raw_text = transcribe(audio)
    final_text = clean_text(raw_text)
    return {
        "call_id": call_id,
        "transcript" : final_text
    }