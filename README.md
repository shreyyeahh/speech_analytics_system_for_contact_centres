## 🎧 AI-Powered Contact Center Intelligence System

An end-to-end Speech Intelligence Platform that analyzes customer support calls using Automatic Speech Recognition (ASR), Sentiment Analysis, and Speech Emotion Recognition, and applies a Decision Engine to determine escalation or resolution actions.

This project simulates how modern cloud contact centers analyze customer calls in real time to improve customer experience and agent efficiency.

**Audio Call (WAV)
      ↓
Automatic Speech Recognition (ASR)
      ↓
Text Transcript
      ↓
Sentiment Analysis (Text-based)
      ↓
Speech Emotion Recognition (Audio-based)
      ↓
Decision Engine (Business Rules)
      ↓
Actionable Insights (Escalate / Normal / Alert)**


**Datasets Used**

RAVDESS – Speech Emotion Recognition
(Angry, Fearful, Sad, Calm voices)

Synthetic & real recorded calls for ASR + sentiment testing


project_root/
│
├── main.py                 # FastAPI entry point
├── pipeline/
│   └── orchestrator.py     # System control flow
│
├── asr/                    # Speech to text
├── nlp/                    # Sentiment analysis
├── emotion/                # Speech emotion recognition
├── decision_engine/        # Escalation logic
│
├── dashboard/              # Streamlit UI
├── models/                 # Saved ML models
├── temp_uploads/           # Uploaded audio
└── requirements.txt


| Layer            | Technology                   |
| ---------------- | ---------------------------- |
| UI               | Streamlit                    |
| API              | FastAPI                      |
| ASR              | Whisper                      |
| NLP              | HuggingFace Transformers     |
| Emotion ML       | Librosa, NumPy, Scikit-learn |
| Model Storage    | Joblib                       |
| Backend          | Python                       |
| Deployment-ready | Modular architecture         |


▶️ How to Run-

1️⃣ Install dependencies
pip install -r requirements.txt

2️⃣ Start backend API
uvicorn main:app --reload

3️⃣ Launch dashboard
streamlit run dashboard/app.py

4️⃣ Upload a WAV call and analyze
