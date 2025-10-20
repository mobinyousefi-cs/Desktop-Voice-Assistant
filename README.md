# Desktop Voice Assistant (Python)

A clean, modular desktop voice assistant with **Tkinter GUI**,
**speech-to-text** (SpeechRecognition + Google Web API), **text-to-speech** (pyttsx3), and a **skill** system (weather, Wikipedia/WolframAlpha, web search, jokes, simple file ops, safe system actions, optional SMTP email).

> Built with a professional `src/` layout, pytest, and CI (Ruff + Black + PyTest).

## ✨ Features
- Push-to-talk microphone capture or manual text input
- Natural voice feedback via `pyttsx3`
- Weather via `wttr.in` JSON (zero keys)
- Wikipedia summaries; fallback to WolframAlpha when configured
- Open a web search in your default browser
- Programming jokes via `pyjokes`
- Safe file manager preview & folder open
- Guarded system actions (sleep) — **off by default**
- Optional SMTP mail sending (**off by default**)

## 🧱 Project Structure
```
src/voice_assistant/
  app.py        # main wiring (CLI/GUI)
  gui.py        # Tkinter UI
  intents.py    # lightweight intent parsing
  tts.py, stt.py
  skills/       # modular skills
```

## 🚀 Quickstart
```bash
python -m venv .venv && source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -e .
voice-assistant --gui   # or: python -m voice_assistant.app --cli
```

> **Microphone permissions**: on macOS and Windows you may need to allow terminal/app access to the microphone.

## 🔧 Configuration
Set environment variables (create a `.env` file if you like):

```env
# Locale & defaults
VA_LOCALE=en-US
VA_DEFAULT_CITY=Rome

# Text-to-speech tuning
VA_TTS_RATE=180
VA_TTS_VOLUME=1.0
VA_TTS_VOICE=Zira      # example: contains name substring

# WolframAlpha (optional)
WOLFRAM_APP_ID=your_app_id

# Enable risky actions explicitly (defaults are OFF)
VA_ALLOW_SYSTEM_POWER=0
VA_ALLOW_EMAIL=0

# SMTP settings (used only if VA_ALLOW_EMAIL=1)
VA_SMTP_HOST=smtp.example.com
VA_SMTP_PORT=587
VA_SMTP_USER=user@example.com
VA_SMTP_PASSWORD=app_password
VA_EMAIL_SENDER=user@example.com
```

## 🗣️ Usage Examples
- "what's the time"
- "weather in Rome"
- "wikipedia Alan Turing"
- "search network slicing 6G"
- "tell me a joke"

## 🛡️ Safety
- Destructive/system-level actions are **disabled by default** and require explicit opt-in via env flags.
- Email functionality is also disabled unless configured.

## 🧪 Tests
```bash
pytest -q
```

## 📝 License
MIT — see `LICENSE`.