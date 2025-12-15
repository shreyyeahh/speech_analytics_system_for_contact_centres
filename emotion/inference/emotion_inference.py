import joblib
import numpy as np
from ..training.config import MODEL_PATH, EMOTION_LABELS
from .audio_preprocessing import preprocess_audio


emotion_model = joblib.load(MODEL_PATH)

def predict_emotion(audio_path):
     
     features = preprocess_audio(audio_path)
     probabilities = emotion_model.predict_proba(features)[0] # here .predict_proba gives probabilities for each class and (features)[0] gives the first feature set
     predicted_index = np.argmax(probabilities)

     return{
          'emotion' : EMOTION_LABELS[predicted_index],
          'confidence' : float(probabilities[predicted_index]),
          'probabilities' : {EMOTION_LABELS[i]: float(probabilities[i]) for i in range(len(EMOTION_LABELS))}
     }