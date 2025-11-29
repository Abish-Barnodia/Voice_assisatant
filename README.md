<<<<<<< HEAD
# Voice Assistant Web App (Python + Gemini)

A modern voice assistant web application with a Python (Flask) backend using Google Gemini AI for responses, and a stylish, animated frontend with voice input and text-to-speech.

## Features
- Modern, animated web UI (HTML/CSS/JS)
- Voice input (browser speech recognition)
- Text-to-speech for assistant replies
- Chat bubble UI (user/assistant)
- Python backend (Flask) with Google Gemini AI
- Special commands: "stop the program", "exit", "your name", "how old are you", "time"
- CORS enabled for frontend-backend communication

## Requirements
- Python 3.12 (use `venv312`)
- Node.js (optional, for static server)
- Google Gemini API key
- Modern web browser (Chrome recommended for speech recognition)

## Setup

### 1. Clone the repository
```
git clone <your-repo-url>
cd <project-folder>
```

### 2. Create and activate Python 3.12 virtual environment
```
python -m venv venv312
./venv312/Scripts/Activate.ps1  # On Windows PowerShell
```

### 3. Install Python dependencies
```
pip install flask flask-cors google-generativeai pyttsx3 SpeechRecognition
```

### 4. Set your Google Gemini API key
- Edit `backend.py` and set your API key:
  ```python
  GOOGLE_API_KEY = "<your-gemini-api-key>"
  ```

### 5. Run the backend
```
python backend.py
```
- The backend will start at `http://127.0.0.1:5000`

### 6. Open the frontend
- Open `assistant_frontend.html` in your browser (Chrome recommended).
- Use the mic button to speak, or type and press Enter.
- The assistant will reply in both text and voice.

## Project Structure
```
.
├── backend.py                # Flask backend (Gemini AI)
├── assistant_frontend.html   # Main web UI
├── assistant_frontend.css    # Styles for web UI
├── assistant_frontend.js     # Frontend logic (chat, mic, TTS)
├── venv312/                  # Python 3.12 virtual environment
└── README.md                 # This file
```

## Notes
- The mic will keep listening until you say "stop the program" or click the stop button.
- For best results, use Google Chrome for speech recognition.
- Do not use Python 3.14+ (incompatible with SpeechRecognition).

## License
MIT License
=======
# Voice_Asssistant-
>>>>>>> 89627ea06c03a23ef2d86130fb103f4481559ff1
