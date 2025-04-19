# Grammar Scoring Engine

## Overview

The **Grammar Scoring Engine** is an application built using **Streamlit**, **Whisper** (for audio transcription), and **Transformers** (for grammar analysis). The app allows users to upload an audio file, get an automatic transcription, evaluate the grammar of the transcript, and see a corrected version with highlighted errors.

---

## Requirements

This project requires **FFmpeg** to process audio files. Below are the steps for installing FFmpeg on different platforms. Please make sure that FFmpeg is correctly installed before running the application.

---

## Installing FFmpeg

### On Windows:
1. Download FFmpeg from the [official FFmpeg website](https://ffmpeg.org/download.html).
2. Extract the contents of the zip file to a directory on your computer.
3. Add the `bin` directory (inside the FFmpeg folder) to your system's **PATH**:
   - Right-click on `This PC` or `My Computer`, and choose **Properties**.
   - Click on **Advanced system settings** and go to the **System Properties** window.
   - Click on the **Environment Variables** button.
   - Under **System Variables**, find the **Path** variable, and click **Edit**.
   - Add the path to the `bin` directory inside your FFmpeg folder (e.g., `C:\ffmpeg\bin`).
4. Verify the installation by opening a command prompt and typing:
   ```bash
   ffmpeg -version
5. if you are still having the issue go through any installation video on youtube for installig it will work 
