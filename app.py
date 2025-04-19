import streamlit as st
import tempfile
import os
from grammar_scorer import score_grammar
from whisper_transcriber import transcribe_whisper
import warnings

import subprocess


warnings.filterwarnings("ignore", category=FutureWarning)  # For Hugging Face
warnings.filterwarnings("ignore", message="FP16 is not supported")  # For Whisper

# Configure Streamlit
st.set_page_config(
    page_title="Grammar Scoring Engine",
    page_icon="✍️",
    layout="wide"
)
try:
    result = subprocess.run(["ffmpeg", "-version"], capture_output=True, text=True)
    if result.returncode == 0:
        st.success("✅ FFmpeg is available!")
        st.text(result.stdout.split('\n')[0])  # Show just the version
    else:
        st.error("❌ FFmpeg not working properly.")
        st.text(result.stderr)
except Exception as e:
    st.error("⚠️ Error when checking FFmpeg:")
    st.text(str(e))
# Custom CSS for better visuals
st.markdown("""
<style>
    .error-highlight {
        background-color: #ffcccc;
        padding: 2px;
        border-radius: 3px;
    }
    .correction-highlight {
        background-color: #ccffcc;
        padding: 2px;
        border-radius: 3px;
    }
    .metric-card {
        border-left: 5px solid #4CAF50;
        padding: 10px;
        background-color: #f9f9f9;
        border-radius: 5px;
        margin-bottom: 20px;
    }
</style>
""", unsafe_allow_html=True)

# App Header
st.title("🎤 Grammar Scoring Engine")
st.markdown("""
Upload an audio file to get:
1. Automatic transcription  
2. Grammar evaluation (0-10 score)  
3. Corrected version with highlighted errors  
""")

# File Upload Section
with st.expander("📁 Upload Audio", expanded=True):
    audio_file = st.file_uploader(
        "Choose an audio file (MP3, WAV, etc.)",
        type=["mp3", "wav", "ogg", "m4a"],
        label_visibility="collapsed"
    )

# Processing Logic
if audio_file:
    # Audio Preview
    st.audio(audio_file, format=f"audio/{audio_file.type.split('/')[-1]}")

    if st.button("🔍 Analyze Grammar", type="primary", use_container_width=True):
        with st.spinner("Processing... (This may take 1-2 minutes)"):
            try:
                # Save to temp file
                with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp:
                    tmp.write(audio_file.read())
                    temp_path = tmp.name

                # Step 1: Transcribe Audio
                transcript = transcribe_whisper(temp_path)

                # Step 2: Grammar Analysis
                score, corrected_text, highlighted_text = score_grammar(transcript)

                # Display Results
                col1, col2 = st.columns(2)

                with col1:
                    st.subheader("📜 Original Transcript")
                    st.markdown(
                        f'<div style="border:1px solid #e6e6e6; padding:15px; border-radius:5px">{transcript}</div>',
                        unsafe_allow_html=True
                    )

                with col2:
                    st.subheader("✨ Corrected Version")
                    st.markdown(
                        f'<div style="border:1px solid #e6e6e6; padding:15px; border-radius:5px">'
                        f'{highlighted_text}'
                        f'</div>',
                        unsafe_allow_html=True
                    )

                # Score Card
                st.markdown("---")
                st.markdown(f"""
                <div class="metric-card">
                    <h2 style="color:#4CAF50; margin-top:0;">Grammar Score: {score}/10</h2>
                    <div style="background:linear-gradient(90deg, #4CAF50 {score*10}%, #e0e0e0 {score*10}%); 
                                height:10px; border-radius:5px;"></div>
                </div>
                """, unsafe_allow_html=True)

                # Improvement Tips
                if score < 8:
                    st.info("💡 **Tips to Improve**:\n"
                            "- Review subject-verb agreement\n"
                            "- Check verb tenses\n"
                            "- Add articles (a/an/the) where needed")

            except Exception as e:
                st.error(f"❌ Processing failed: {str(e)}")
            finally:
                if os.path.exists(temp_path):
                    os.unlink(temp_path)

# Footer
st.markdown("---")
st.caption("""
Built with ♥ using [Whisper](https://openai.com/research/whisper), 
[Transformers](https://huggingface.co/), and 
[Streamlit](https://streamlit.io/)
""")
