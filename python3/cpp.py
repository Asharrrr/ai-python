import streamlit as st
from gtts import gTTS
import os

st.title("🗣️ AI-Powered Free Text-to-Speech Converter")
st.write("Enter text below and click 'Convert to Speech' to hear it.")

# User Input
user_input = st.text_area("Enter text to convert:")

if st.button("Convert to Speech"):
    if user_input:
        # Convert text to speech
        tts = gTTS(text=user_input, lang='en')
        tts.save("output.mp3")
        
        # Play the generated speech
        st.audio("output.mp3", format="audio/mp3")
        
        st.success("Speech generated successfully! ✅")
    else:
        st.warning("Please enter some text before converting.")

