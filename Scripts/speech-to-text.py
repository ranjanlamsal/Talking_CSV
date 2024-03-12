# speech_to_text.py
# Load environment variables from .env file

import pyaudio
import wave
from openai import OpenAI
import os
import pyttsx3
from csvreader import prompt_response
from dotenv import load_dotenv
import gtts
from playsound import playsound
import streamlit as st

# Load environment variables from .env file
load_dotenv()

api_key = os.environ.get('OPENAI_API_KEY')


# Function to record audio from the microphone
def record_audio(filename, duration=10, sample_rate=44100, chunk_size=1024):
    """
    Records audio from the microphone and saves it to a WAV file.

    Parameters:
        filename (str): The name of the WAV file to save the recorded audio.
        duration (int): Duration of the recording in seconds (default is 10 seconds).
        sample_rate (int): Sampling rate of the audio (default is 44100 Hz).
        chunk_size (int): Size of each chunk of audio data to be read (default is 1024 bytes).

    Returns:
        None
    """
    
    audio = pyaudio.PyAudio()
    stream = audio.open(format=pyaudio.paInt16,
                        channels=1,
                        rate=sample_rate,
                        input=True,
                        frames_per_buffer=chunk_size)

    print("Recording...")
    frames = []
    for _ in range(0, int(sample_rate / chunk_size * duration)):
        data = stream.read(chunk_size)
        frames.append(data)
    print("Finished recording.")

    stream.stop_stream()
    stream.close()
    audio.terminate()

    # Save the recorded audio to a WAV file
    with wave.open(filename, 'wb') as wf:
        wf.setnchannels(1)
        wf.setsampwidth(audio.get_sample_size(pyaudio.paInt16))
        wf.setframerate(sample_rate)
        wf.writeframes(b''.join(frames))
        

# Function to transcribe audio using Whisper AI
def transcribe_audio(filename):
    """
    Transcribes audio using OpenAI's Whisper AI.

    Parameters:
        filename (str): The name of the WAV file containing the audio to transcribe.

    Returns:
        str: Transcribed text from the audio.
    """
    
    client = OpenAI()

    audio_file= open(filename, "rb")
    transcription = client.audio.transcriptions.create(
    model="whisper-1", 
    file=audio_file
    )
    return transcription.text

def text_to_speech(text):
    """
    Converts text to speech using Google Text-to-Speech and saves it as an MP3 file.

    Parameters:
        text (str): The text to convert to speech.

    Returns:
        None
    """
    
    # initialize Text-to-speech engine
    engine = pyttsx3.init()
    
    # convert text to speech
    engine.say(text)
    # play the speech
    engine.runAndWait()
    
def text_to_speech2(text, filepath):
    # make request to google to get synthesis
    tts = gtts.gTTS("Hello world")
    
    # make request to google to get synthesis
    tts = gtts.gTTS(text)
    
    # save the audio file
    tts.save(filepath)


# app.py
def main():
    st.title("Talking CSV")

    # File upload section
    st.write("Upload your CSV file:")
    uploaded_file = st.file_uploader("Choose a CSV file", type=["csv"])

    if uploaded_file is not None:
        st.success("File uploaded successfully.")
        file_details = {"FileName": uploaded_file.name, "FileType": uploaded_file.type, "FileSize": uploaded_file.size}
        st.write(file_details)
        
         # Create directory if it doesn't exist
        os.makedirs("../user-csv", exist_ok=True)
        os.makedirs("../Audio/Input", exist_ok=True)
        os.makedirs("../Audio/Output", exist_ok=True)
         
        # Save uploaded file to local storage
        csv_filepath = os.path.join("../user-csv", uploaded_file.name)
        with open(csv_filepath, "wb") as f:
            f.write(uploaded_file.getbuffer())
            f.close()
        
        input_audio_file = os.path.join("../Audio/Input/audio.wav")
        output_audio_file = os.path.join("../Audio/Output/response.mp3")
        
        st.write("Click the button below to start recording your voice.")

        if st.button("Record"):
            st.write("RECORDING.................")
        
            record_audio(input_audio_file)
            st.success("Recording finished.")

            st.write("Transcribing audio...")
            text = transcribe_audio(input_audio_file)
            st.success("Transcription complete.")

            response_text = prompt_response(text, csv_filepath)
            
            st.write("Response:")
            response_audio = text_to_speech2(response_text, output_audio_file)
            st.audio(output_audio_file, format='audio/mp3')

if __name__ == "__main__":
    main()
