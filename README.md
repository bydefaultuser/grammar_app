# 🎤 Grammar Scoring Engine

This project leverages **OpenAI's Whisper** for speech-to-text and **Hugging Face Transformers** for grammar correction. It's wrapped in a simple and interactive **Streamlit UI** that allows users to:

- 📄 **Automatically transcribe** audio files (MP3, WAV, etc.)
- ✍️ **Evaluate grammar** and generate corrections
- 🧠 **Score** the grammar quality out of 10

---

## 🔧 Tech Stack

- **Streamlit** — For the interactive web interface
- **OpenAI Whisper** — For high-quality speech recognition
- **HuggingFace Transformers** (`vennify/t5-base-grammar-correction`) — For grammar correction
- **Python**

---

## 🚀 Run Locally

### 1. Clone the Repository
```bash
git clone https://github.com/bydefaultuser/grammar_app.git
cd grammar_app
