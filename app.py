import streamlit as st
from modules.text_extractor import extract_text
from modules.llm_processor import rewrite_text_for_audiobook
from modules.tts_engine import text_to_speech
import streamlit.components.v1 as components


st.title("AI Audiobook Generator")

uploaded_file = st.file_uploader(
    "Upload Document",
    type=["pdf", "docx", "txt"]
)

if uploaded_file:
    st.info("📄 Extracting text...")
    text = extract_text(uploaded_file, uploaded_file.name)

    st.success("Text Extracted ✅")
    st.text_area("Extracted Text", text, height=300)

if uploaded_file:

    if st.button("Rewrite with AI and Generate Audiobook 🎧"):

        status = st.status("Rewriting with AI...", expanded=True)
        with status: 
            new_text = rewrite_text_for_audiobook(text) 
            status.update(label="✅ AI rewriting completed!", state="complete")
        st.text_area("Audiobook Style Text", new_text, height=300)

        status = st.status("Generating Audiobook 🎧...", expanded=True)
        with status: 
            audio_file = text_to_speech(new_text)
            status.update(label="🎧 Audiobook generated successfully!", state="complete")
        st.audio(audio_file)

        with open("avatar_player.html", "r", encoding="utf-8") as f:
            avatar_html = f.read()
        avatar_html = avatar_html.replace("audiobook.mp3", audio_file)
        components.html(avatar_html, height=600)    

        with open(audio_file, "rb") as f:
            st.download_button(
                "Download Audiobook",
                f,
                file_name="audiobook.mp3"
            ) 


