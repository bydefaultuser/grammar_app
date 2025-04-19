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
If FFmpeg is installed correctly, it will show the version information.

On macOS:
Install Homebrew if you haven't already:

bash
Copy
Edit
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
Install FFmpeg using Homebrew:

bash
Copy
Edit
brew install ffmpeg
Verify the installation by typing the following in the terminal:

bash
Copy
Edit
ffmpeg -version
On Linux (Ubuntu/Debian):
Run the following commands to install FFmpeg:

bash
Copy
Edit
sudo apt update
sudo apt install ffmpeg
Verify the installation by typing:

bash
Copy
Edit
ffmpeg -version
Installation Video
For a detailed guide on how to install FFmpeg on your system, watch this YouTube video.

Installation
Clone the Repository
Clone the repository to your local machine using Git:

bash
Copy
Edit
git clone https://github.com/your-username/grammar-scoring-engine.git
Install Dependencies
Navigate to the project folder and install the required Python dependencies:

bash
Copy
Edit
cd grammar-scoring-engine
pip install -r requirements.txt
Running the Application
Once all dependencies are installed, run the app using the following command:

bash
Copy
Edit
streamlit run app.py
How It Works
Audio File Upload: Upload an audio file in MP3, WAV, OGG, or M4A format using the app interface.

Audio Transcription: The app uses Whisper to transcribe the uploaded audio into text.

Grammar Scoring: The transcript is analyzed for grammar, and a score (out of 10) is generated using the Transformers library.

Corrections: The app shows a corrected version of the transcript with highlighted grammar errors.

Improvement Tips: If the grammar score is below 8, the app will suggest tips for improving grammar, such as subject-verb agreement, verb tense checks, and article usage.

Troubleshooting
If FFmpeg is not working correctly, make sure it is installed properly and added to the system PATH (for Windows).

If you encounter issues with audio transcription or grammar scoring, ensure that the dependencies are correctly installed using the pip install -r requirements.txt command.

Additional Information
For more details on Whisper, Transformers, or Streamlit, you can refer to the following official documentation:

Whisper

Transformers

Streamlit

Built With
Whisper for transcription

Transformers for grammar analysis

Streamlit for the web app interface

License
This project is licensed under the MIT License - see the LICENSE file for details.

markdown
Copy
Edit
