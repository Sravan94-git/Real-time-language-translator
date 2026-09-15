# 🌍 Voxa Real-Time Language Translator

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Framework](https://img.shields.io/badge/Framework-Flask-black.svg)](https://flask.palletsprojects.com/)
[![Translation](https://img.shields.io/badge/API-MyMemory-green.svg)](https://mymemory.translated.net/)
[![Speech Recognition](https://img.shields.io/badge/SpeechRecognition-Browser-blue.svg)](https://developer.mozilla.org/en-US/docs/Web/API/SpeechRecognition)

**Voxa** is a Flask-based real-time language translation workspace. It accepts typed text or browser microphone input, translates it into the selected language, and generates spoken audio for the translation using Google Text-to-Speech. The responsive interface also supports copying, playing, and stopping translated audio.

***

## ✨ Key Features

- 🎤 **Browser Voice Input:** Captures live voice input using the browser Speech Recognition API.
- 🌍 **Multi-Language Translation:** Supports translation between 100+ languages.
- 🔊 **Text-to-Speech Conversion:** Converts translated text into natural speech.
- 💻 **Responsive Flask Interface:** Clean web application for desktop and mobile screens.
- 📝 **Live Text Display:** Displays recognized and translated text instantly.
- ▶️ **Audio Controls:** Play and stop translated speech from either workspace.
- 🌐 **Language Selection:** Choose both source and destination languages.
- 🛡️ **Security Protections:** Includes request limits, rate limiting, security headers, and generic public errors.
- 🚀 **Cloud Deployment:** Configured for Vercel serverless deployment and traditional Gunicorn hosting.

***

## 🛠️ Tech Stack

- **Programming Language:** Python 3
- **Backend Framework:** Flask
- **Frontend:** HTML, CSS, and browser JavaScript
- **Speech Recognition:** Browser Speech Recognition API
- **Translation API:** MyMemory through deep-translator
- **Text-to-Speech:** Google Text-to-Speech (gTTS)
- **Production Server:** Gunicorn
- **Deployment:** Vercel or any Gunicorn-compatible host

***

## 🚀 Project Workflow

1. User selects the source and target languages.
2. User types text or uses the browser microphone.
3. The browser converts speech into text when voice input is used.
4. Flask validates the request and calls the translation service.
5. The translated text is displayed on the screen.
6. User can copy the result or request spoken audio.
7. Google Text-to-Speech generates an MP3 response.
8. User can play or stop the translated audio.

***

## 📂 Project Structure

```text
Real-Time-Language-Translator/
│
├── main.py
├── requirements.txt
├── README.md
├── Procfile
├── vercel.json
├── api/
│   └── index.py
├── static/
│   └── style.css
├── templates/
│   └── index.html
│
└── .gitignore
```

***

## 📊 Applications

- 🌍 Real-Time Language Translation
- ✈️ Travel Assistance
- 🎓 Language Learning
- 💼 Business Communication
- 🏥 Healthcare Communication
- 📞 Customer Support
- 🤖 AI Voice Assistants
- 🗣️ Cross-Language Conversations

***

## 🎯 Future Enhancements

- 📹 Real-time video translation.
- 📱 Mobile application support.
- 🌐 Offline translation mode.
- 🤖 AI-powered speech enhancement.
- 🎙️ Speaker identification.
- 📄 Translation history and export.
- ☁️ Cloud deployment with authentication and shared rate limiting.
- 📊 Translation analytics dashboard.

***

## 💻 Installation

### Clone the Repository

```bash
git clone https://github.com/Sravan94-git/Real-time-language-translator.git

cd Real-time-language-translator
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run the Application

```bash
python main.py
```

Open your browser and visit:

```
http://127.0.0.1:5000
```

***

## 📸 Output

- Select source and target languages.
- Type text or click **Speak** and allow microphone access.
- Click **Translate**.
- The application displays:
  - 🎤 Recognized Speech
  - 🌍 Translated Text
  - 🔊 Play and stop controls for the translation audio

***

## 📈 Results

- Browser-based speech recognition where supported by Chrome and Edge.
- Multilingual translation across 100+ languages.
- Natural voice output using Google Text-to-Speech.
- Responsive and user-friendly Flask interface.
- Server-side validation and abuse protections for public endpoints.
- Efficient solution for real-time multilingual communication.

***

## 📦 Requirements

```text
Flask==3.1.3
deep-translator==1.11.4
gTTS==2.5.4
gunicorn==23.0.0
```

Install all dependencies using:

```bash
pip install -r requirements.txt
```

### Production Server

```bash
gunicorn main:app
```

### Vercel Deployment

The repository includes `api/index.py` and `vercel.json` for Vercel's Python serverless runtime. Import the GitHub repository into Vercel and deploy without a separate start command.

***

## 🤝 Contributing

Contributions are welcome!

Feel free to fork the repository, create a feature branch, and submit a pull request.

***

## 📜 License

This project is licensed under the **MIT License**.

***

## 👨‍💻 Author

**Sravan**

AI | Machine Learning | Deep Learning | Python Developer | Full Stack Developer

If you found this project useful, don't forget to ⭐ the repository!
