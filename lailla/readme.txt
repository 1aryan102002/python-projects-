# Lylla - Python Voice Assistant

Lylla is a Python-based voice assistant that can recognize speech, play music, fetch news, open websites, and chat using OpenAI’s GPT models.

## Features

- **Speech Recognition:** Listens for the wake word ("laila") and processes voice commands.
- **Text-to-Speech:** Responds using natural-sounding speech.
- **Music Search:** Plays songs using YouTube links.
- **News Headlines:** Reads out the top 5 news headlines for India.
- **Web Automation:** Opens popular websites (Google, YouTube, LinkedIn, Instagram, ChatGPT).
- **AI Chat:** Answers questions and chats using OpenAI’s GPT-4o model.
- **Shutdown Command:** Ends the session with a voice command.

## File Overview

- **main.py**  
  The main application file. Handles speech recognition, command processing, text-to-speech, and integrates all features.

- **music.py**  
  (Assumed) Contains logic for searching and retrieving music links.

## Setup Instructions

1. **Clone the repository:**
   ```
   git clone <your-repo-url>
   cd lylla_python-mega-project-001
   ```

2. **Install dependencies:**
   ```
   pip install speechrecognition pyttsx3 requests openai
   ```
   *(You may also need `PyAudio` for microphone access: `pip install pyaudio`)*

3. **API Keys:**
   - Replace `NEWS_API_KEY` in `main.py` with your own [NewsAPI](https://newsapi.org/) key.
   - Replace `openai_api_key` with your OpenAI API key.

4. ## Application Launcher Feature

Lylla can run any application on your Windows PC using voice commands.

**How to use:**
- Say: `run C:\Path\To\Application.exe`
- Lylla will check if the file exists and launch it for you.

**Example:**
- `run C:\Windows\System32\notepad.exe`  
  Lylla will open Notepad.

**Note:**  
- Make sure to provide the full path to the application.
- This feature works only on Windows (uses `os.startfile())
   ```
   python main.py
   ```

## Usage

- Say "laila" to activate the assistant.
- Give commands like:
  - "open google"
  - "play [song name]"
  - "news"
  - "shutdown"
  - Or ask any question for AI chat.

## Notes

- Make sure your microphone is working.
- You can customize the wake word and responses in `main.py`.
- For music playback, ensure `music.py` is present and properly configured.


