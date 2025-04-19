import whisper
import numpy as np

def transcribe_whisper(audio_path):
    """Transcribes audio using Whisper (with FFmpeg fallback)."""
    model = whisper.load_model("base")
    
    # Load audio (avoids FFmpeg if possible)
    try:
        audio = whisper.load_audio(audio_path)
        audio = whisper.pad_or_trim(audio)
        mel = whisper.log_mel_spectrogram(audio).to(model.device)
        result = model.transcribe(mel)
        return result["text"]
    except Exception:
        # Fallback to direct model transcribe (requires FFmpeg)
        result = model.transcribe(audio_path)
        return result["text"]