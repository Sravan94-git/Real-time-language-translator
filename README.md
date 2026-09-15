# 🌍 Real-Time Language Translator using Speech Recognition & Google Translate

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Framework](https://img.shields.io/badge/Framework-Streamlit-red.svg)](https://streamlit.io/)
[![Translation](https://img.shields.io/badge/API-Google%20Translate-green.svg)](https://translate.google.com/)
[![Speech Recognition](https://img.shields.io/badge/SpeechRecognition-Google-blue.svg)](https://pypi.org/project/SpeechRecognition/)

This project presents an **AI-powered Real-Time Language Translator** that enables users to translate spoken language into another language instantly. Built using **Python**, **Streamlit**, **SpeechRecognition**, **Google Translate**, and **Google Text-to-Speech (gTTS)**, the application captures voice input through a microphone, converts it into text, translates it into the selected language, and generates natural-sounding speech for the translated output. The application offers an intuitive web interface for seamless multilingual communication.

***

## ✨ Key Features

- 🎤 **Real-Time Speech Recognition:** Captures live voice input using a microphone.
- 🌍 **Multi-Language Translation:** Supports translation between 100+ languages.
- 🔊 **Text-to-Speech Conversion:** Converts translated text into natural speech.
- 💻 **Interactive Streamlit Interface:** Easy-to-use web application.
- 📝 **Live Text Display:** Displays recognized and translated text instantly.
- ⚡ **Fast Translation:** Provides near real-time speech translation.
- 🌐 **Language Selection:** Choose both source and destination languages.
- 🚀 **Lightweight Deployment:** Easy to run locally or deploy on cloud platforms.

***

## 🛠️ Tech Stack

- **Programming Language:** Python 3
- **Frontend Framework:** Streamlit
- **Speech Recognition:** SpeechRecognition (Google Speech API)
- **Translation API:** Google Translate (googletrans)
- **Text-to-Speech:** Google Text-to-Speech (gTTS)
- **Audio Processing:** PyAudio
- **Development Environment:** VS Code, Jupyter Notebook

***

## 🚀 Project Workflow

1. User selects the source and target languages.
2. User clicks the **Start Translation** button.
3. The application listens to the user's speech.
4. SpeechRecognition converts the spoken audio into text.
5. Google Translate translates the recognized text.
6. The translated text is displayed on the screen.
7. Google Text-to-Speech converts the translated text into speech.
8. The translated audio is played directly within the application.

***

## 📂 Project Structure

```text
Real-Time-Language-Translator/
│
├── app.py
├── requirements.txt
├── README.md
│
├── assets/
│   └── screenshots/
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
- ☁️ Cloud deployment with authentication.
- 📊 Translation analytics dashboard.

***

## 💻 Installation

### Clone the Repository

```bash
git clone https://github.com/yourusername/Real-Time-Language-Translator.git

cd Real-Time-Language-Translator
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Install PyAudio (If Required)

#### Windows

```bash
pip install pipwin
pipwin install pyaudio
```

#### Linux

```bash
sudo apt-get install portaudio19-dev
pip install pyaudio
```

#### macOS

```bash
brew install portaudio
pip install pyaudio
```

### Run the Application

```bash
streamlit run app.py
```

Open your browser and visit:

```
http://localhost:8501
```

***

## 📸 Output

- Select source and target languages.
- Click **Start Translation**.
- Speak into the microphone.
- The application displays:
  - 🎤 Recognized Speech
  - 🌍 Translated Text
  - 🔊 Audio Playback of the Translation

***

## 📈 Results

- Accurate speech recognition using Google's Speech API.
- Fast multilingual translation across 100+ languages.
- Natural voice output using Google Text-to-Speech.
- Responsive and user-friendly Streamlit interface.
- Efficient solution for real-time multilingual communication.

***

## 📦 Requirements

```text
streamlit
SpeechRecognition
googletrans==4.0.0rc1
gTTS
PyAudio
```

Install all dependencies using:

```bash
pip install -r requirements.txt
```

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
