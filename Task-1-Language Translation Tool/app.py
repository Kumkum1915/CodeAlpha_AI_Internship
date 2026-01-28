import streamlit as st
from deep_translator import GoogleTranslator

# Page settings
st.set_page_config(page_title="AI Language Translation Tool", layout="centered")

st.title("🌍 AI Language Translation Tool")
st.write("Translate text between different languages using Artificial Intelligence.")

# Input text
text = st.text_area("Enter text to translate")

# Language selection
languages = {
    "English": "en",
    "Hindi": "hi",
    "French": "fr",
    "Spanish": "es",
    "German": "de",
    "Chinese": "zh-CN",
    "Japanese": "ja",
    "Korean": "ko",
    "Arabic": "ar"
}

source_language = st.selectbox("Select source language", list(languages.keys()))
target_language = st.selectbox("Select target language", list(languages.keys()), index=1)

# Translate button
if st.button("Translate"):
    if text.strip() == "":
        st.warning("⚠️ Please enter text to translate.")
    else:
        translated_text = GoogleTranslator(
            source=languages[source_language],
            target=languages[target_language]
        ).translate(text)

        st.subheader("Translated Text")
        st.success(translated_text)

        # Copy option
        st.code(translated_text)

        
