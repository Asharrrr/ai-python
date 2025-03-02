import pyttsx3
import streamlit as st

# Custom CSS to apply background color
st.markdown("### *Textoolex*", unsafe_allow_html=True)


st.markdown(
    """
    <style>
    /* Set background color for the main content */
    .stApp {
        background-color: #90EE90; /* Light Green */
    }
    
    /* Change text color to black for better visibility */
    .stMarkdown, .stTextInput, .stTitle {
        color: black;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("📄 AI-Powered Free Text-to-Speech Converter")
st.write("By Muhammad Ashar Founder Of texttoolex")
st.subheader("Press Enter to Run Your Text into Speech")

# User input
user_input = st.text_input("Enter text to convert:")

# Convert text to speech
if user_input.strip():  # Ensures input is not just spaces
    engine = pyttsx3.init()
    engine.say(user_input)
    engine.runAndWait()
    st.success("Speech generated successfully! ✅")
else:
    st.warning("Please enter some text to convert!")  # Display warning if no input



import streamlit as st

# Title and Introduction
st.title("All About the Text-To-Speech Converter AI Agent")

st.subheader("Introduction")
st.write('''
In today's digital world, accessibility and convenience are key to enhancing user experiences. 
One of the most significant innovations in this area is Text-to-Speech (TTS) conversion. 
TTS technology allows computers to convert written text into spoken words, making information more 
accessible to everyone, including visually impaired individuals and those who prefer listening over reading.
''')

# What is TTS?
st.subheader("What is a Text-to-Speech Converter?")
st.write('''
A Text-to-Speech (TTS) converter is a tool that takes text as input and converts it into 
natural-sounding speech using artificial intelligence and speech synthesis. 
These tools use **Natural Language Processing (NLP)** and **machine learning algorithms** 
to generate human-like speech, improving accessibility and productivity.
''')

# How TTS Works
st.subheader("How Does TTS Work?")
st.write('''
TTS technology follows a few key steps:
1. **Text Analysis** - The software processes input text and breaks it down into sentences and words.
2. **Linguistic Processing** - It applies pronunciation rules, grammar, and context to generate a natural flow.
3. **Speech Synthesis** - The text is converted into speech using AI-driven voice generation models.
4. **Audio Output** - The synthesized speech is played aloud or saved as an audio file.
''')

# Benefits of TTS
st.subheader("Benefits of Text-to-Speech Technology")
st.write('''
✅ **Accessibility** - Helps visually impaired users access digital content.\n
✅ **Productivity Boost** - Allows users to listen to documents, emails, and articles while multitasking.\n
✅ **Language Learning** - Assists with pronunciation and comprehension for learners.\n
✅ **Entertainment & Gaming** - Provides realistic AI voices for audiobooks, podcasts, and video games.\n
✅ **Customer Service** - Used in chatbots and virtual assistants for automated voice responses.\n
''')

# Future of TTS
st.subheader("The Future of TTS Technology")
st.write('''
With rapid advancements in **AI and deep learning**, TTS technology is evolving to provide 
ultra-realistic voices, personalized speech experiences, and enhanced multilingual support. 
Future innovations may include **emotion-driven speech synthesis, real-time translations, and voice cloning**.
''')

st.success("Try out a TTS converter today and experience the power of AI-driven speech synthesis! 🚀")
