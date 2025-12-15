import streamlit as st
import requests
import tempfile

st.set_page_config(
    page_title = "Multimodal AI Speech Analystics System",
    layout = "centered"
)

st.title(" 📞 Multimodal AI Speech Analytics System")
st.write("Upload an audio file to analyze its transcription, sentiment, and emotion.")


uploaded_file = st.file_uploader("Upload an audio file (.wav)", type=['wav'])

if uploaded_file is not None:
    if st.button("Analyze"):
        st.info("Analyzing the audio file, please wait...")
        with tempfile.NamedTemporaryFile(delete = False, suffix = 'wav') as temp_audio: # Create a temporary file to store the uploaded audio, here delete = False means file will not be deleted when closed and suffix = 'wav' means file extension will be .wav , tempfile.NamedTemporaryFile creates a temporary file that can be used as a regular file
            temp_audio.write(uploaded_file.read())
            temp_audio_path = temp_audio.name

        try:
            response = requests.post(
                "http://127.0.0.1:8000/analyze_call/",
                files = {"file": open(temp_audio_path, "rb")} # here we are sending the audio file to the API endpoint as a binary file , we use open(temp_audio_path, "rb") to read the file in binary mode and send it as part of the files parameter in the POST request , the url is the local address where the FastAPI server is running
            )

            if response.status_code == 200:
                data = response.json()

                st.success("Analysis Complete!")

                st.subheader("Transcript")
                st.write(data["transcript"])

                st.subheader("Sentiment Analysis")
                st.write(
                    f"{data['sentiment']['label']}"
                    f"(Confidence: {data['sentiment']['confidence']:.2f})"
                )

                st.subheader("Emotion Detection")
                st.write(
                    f"{data['emotion']['label']}"
                    f"(Confidence:{data['emotion']['confidence']:.2f})"
                )

                st.subheader("Escalation Decision")
                if data["escalation"]["escalate"]:
                    st.error("This call should be escalated.")
                    for reason in data['escalation']['reasons']:
                        st.write(f"- {reason}")
                else:
                    st.success("This call does not need escalation.")


            else:
                st.error(f"Error: {response.status_code} - {response.text}")   
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")                     
