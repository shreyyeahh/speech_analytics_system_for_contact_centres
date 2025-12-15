import os
def validate_audio(audio_path):
    if not os.path.exists(audio_path):
        raise FileNotFoundError("Audi file not found")
    if not audio_path.lower().endswith(('.wav', '.mp3', '.flac')):
        raise ValueError("Unsupported audio format")
    

def load_audio(audio_path):
    validate_audio(audio_path)
    return audio_path 
    
    