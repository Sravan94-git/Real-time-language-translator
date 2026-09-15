import io
import os

from deep_translator.constants import GOOGLE_LANGUAGES_TO_CODES
from deep_translator import MyMemoryTranslator
from flask import Flask, jsonify, render_template, request, send_file
from gtts import gTTS

app = Flask(__name__)
languages = dict(sorted(GOOGLE_LANGUAGES_TO_CODES.items()))
language_codes = set(languages.values())
language_names = {code: name for name, code in languages.items()}


@app.get("/")
def index():
    return render_template("index.html", languages=languages)


@app.post("/api/translate")
def translate():
    data = request.get_json(silent=True) or {}
    text = str(data.get("text", "")).strip()
    source = data.get("source", "auto")
    target = data.get("target", "es")

    if not text:
        return jsonify(error="Enter some text to translate."), 400
    if target not in language_codes:
        return jsonify(error="Select a valid target language."), 400
    if source != "auto" and source not in language_codes:
        return jsonify(error="Select a valid source language."), 400

    try:
        source_name = language_names.get(source, "english")
        target_name = language_names[target]
        translator = MyMemoryTranslator(source=source_name, target=target_name)
        translated_text = translator.translate(text)
        if not translated_text:
            raise ValueError("The translation service returned an empty result.")
        return jsonify(text=translated_text, detected_language=source)
    except Exception as error:
        return jsonify(error=f"Translation service error: {error}"), 502


@app.post("/api/speak")
def speak():
    data = request.get_json(silent=True) or {}
    text = str(data.get("text", "")).strip()
    language = data.get("language", "en")

    if not text:
        return jsonify(error="There is no translated text to speak."), 400
    if language not in language_codes:
        return jsonify(error="Select a valid language for audio."), 400

    try:
        audio = io.BytesIO()
        gTTS(text=text, lang=language, slow=False).write_to_fp(audio)
        audio.seek(0)
        return send_file(audio, mimetype="audio/mpeg", download_name="translation.mp3")
    except Exception as error:
        return jsonify(error=f"Text-to-speech error: {error}"), 502


if __name__ == "__main__":
    app.run(debug=os.getenv("FLASK_DEBUG") == "1")