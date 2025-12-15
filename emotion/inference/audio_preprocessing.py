import librosa
import numpy as np
from emotion.training.config import SAMPLE_RATE, N_MFCC, MAX_DURATION


def load_audio(audio_path):
    """Load an audio file and return the audio time series and sample rate."""
    audio, sr = librosa.load(audio_path, sr=SAMPLE_RATE, mono=True)
    return audio

def fix_audio_length(signal):

    max_length = int(SAMPLE_RATE * MAX_DURATION)

    if len(signal) > max_length:
        return signal[:max_length]
    
    if len(signal)< max_length:
        padding = max_length - len(signal)
        return np.pad(signal,(0,padding)) # Pad with zeros at the end because it's silence
    return signal


def extract_mfcc(signal):

    mfcc = librosa.feature.mfcc(
        y = signal, 
        sr = SAMPLE_RATE,
        n_mfcc = N_MFCC
    )

    mfcc_mean = np.mean(mfcc, axis = 1)
    return mfcc_mean # we are doing mean of mfcc across time axis because we want fixed size input for model

def preprocess_audio(audio_path):
    signal = load_audio(audio_path)
    fixed_signal = fix_audio_length(signal)
    features = extract_mfcc(signal)
    return features.reshape(1,-1)
