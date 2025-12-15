from fastapi import FastAPI, UploadFile, File
import shutil
import uuid
import os
from pipeline.orchestrator import analyze_call

app = FastAPI(
    title = "Speech Analytics System for Contact Centres",
    description = "Speech + Sentiment + Emotion Analysis"
,
version = "1.0"
)

UPLOAD_DIR = "temp_uploads" # Directory to store uploaded files
os.makedirs(UPLOAD_DIR, exist_ok = True) # means create directory if not exists

@app.post("/analyze_call/") # Endpoint to analyze call audio file , method = POST means send data to server , server process data and return response , here server means FastAPI app that we created , which is running on local machine or cloud server
def analyze_call_api(file : UploadFile = File(...)):
    file_id = str(uuid.uuid4())
    file_path = os.path.join(UPLOAD_DIR, f"{file_id}.wav") # Save file with unique id to avoid name conflicts

    with open(file_path, "wb") as buffer: # Write uploaded file to disk, we are opening file in write binary mode because audio files are binary files
        shutil.copyfileobj(file.file, buffer) # Copy file object to buffer so that it can be saved

    result = analyze_call(file_path)
    return result    
