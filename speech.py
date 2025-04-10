# Import necessary libraries
import streamlit as st
import torch
import librosa
import numpy as np
from transformers import Wav2Vec2ForCTC, Wav2Vec2Processor, BartForConditionalGeneration, BartTokenizer

# Cache the models and processor to reduce memory usage
@st.cache_resource  # Use st.cache_resource to load models only once
def load_models():
    processor = Wav2Vec2Processor.from_pretrained("facebook/wav2vec2-base-960h")
    model = Wav2Vec2ForCTC.from_pretrained("facebook/wav2vec2-base-960h")

    tokenizer = BartTokenizer.from_pretrained("sshleifer/distilbart-cnn-12-6")
    summarization_model = BartForConditionalGeneration.from_pretrained("sshleifer/distilbart-cnn-12-6")
    
    return processor, model, tokenizer, summarization_model

# Cache the transcription data
@st.cache_data
def transcribe_audio(audio_data):
    processor, model, _, _ = load_models()
    input_values = processor(audio_data, sampling_rate=16000, return_tensors="pt", padding="longest").input_values
    
    with torch.no_grad():
        logits = model(input_values).logits

    predicted_ids = torch.argmax(logits, dim=-1)
    transcription = processor.batch_decode(predicted_ids)[0]

    return transcription

# Cache the summarization data
@st.cache_data
def summarize_text(text):
    _, _, tokenizer, summarization_model = load_models()
    inputs = tokenizer(text, return_tensors="pt", max_length=1024, truncation=True, padding="longest")
    
    with torch.no_grad():
        summary_ids = summarization_model.generate(
            inputs["input_ids"], 
            max_length=150, 
            min_length=30, 
            length_penalty=2.0, 
            num_beams=4, 
            early_stopping=True
        )
    
    summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)

    return summary

# Streamlit app UI setup
st.set_page_config(page_title="Audio Summarization App", page_icon="🎤", layout="wide")
st.title("Audio Summarization Application")
st.write("This application allows you to upload an audio file and get a summarized transcription of the content. The accuracy of the transcription and summarization depends on the clarity of the voice in the audio.")

# Option to upload an audio file
uploaded_file = st.file_uploader("Upload your audio file (.wav or .mp3)", type=["wav", "mp3"])

if uploaded_file is not None:
    st.audio(uploaded_file, format="audio/wav")
    st.write("Transcribing audio...")

    audio, sr = librosa.load(uploaded_file, sr=16000)
    audio = audio.astype(np.float32)

    transcription = transcribe_audio(audio)
    st.write("**Transcription:**")
    st.success(transcription)

    st.write("Summarizing the transcription...")
    summary = summarize_text(transcription)
    st.write("**Summary:**")
    st.success(summary)

    # Note about accuracy
    st.warning("Note: The accuracy of the transcription and summarization depends on the clarity of the voice in the audio.")
else:
    st.write("Please upload a .wav or .mp3 audio file for transcription and summarization.")

# Add buttons to clear cache manually
if st.button("Clear Cache"):
    st.cache_data.clear()
    st.cache_resource.clear()
    st.write("Cache cleared!")