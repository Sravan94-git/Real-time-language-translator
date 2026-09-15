import io
import os
import time
from collections import defaultdict, deque

from deep_translator.constants import GOOGLE_LANGUAGES_TO_CODES
from deep_translator import MyMemoryTranslator
from flask import Flask, jsonify, render_template, request, send_file
from gtts import gTTS

app = Flask(__name__)
app.config["MAX_CONTENT_LENGTH"] = 20 * 1024
languages = dict(sorted(GOOGLE_LANGUAGES_TO_CODES.items()))
language_codes = set(languages.values())
language_names = {code: name for name, code in languages.items()}
rate_buckets = defaultdict(deque)
rate_limits = {"translate": (30, 60), "speak": (10, 60)}


def is_rate_limited(bucket_name):
    limit, window = rate_limits[bucket_name]
    client_key = request.headers.get("X-Forwarded-For", request.remote_addr or "unknown").split(",")[0].strip()
    now = time.monotonic()
    timestamps = rate_buckets[(bucket_name, client_key)]
    while timestamps and now - timestamps[0] >= window:
        timestamps.popleft()
    if len(timestamps) >= limit:
        return True
    timestamps.append(now)
    return False


@app.after_request
def add_security_headers(response):
    response.headers["X-Content-Type-Options"] = "nosniff"
    response.headers["X-Frame-Options"] = "DENY"
    response.headers["Referrer-Policy"] = "no-referrer"
    response.headers["Permissions-Policy"] = "microphone=(self)"
    response.headers["Content-Security-Policy"] = (
        "default-src 'self'; script-src 'self' 'unsafe-inline'; style-src 'self' 'unsafe-inline'; "
        "connect-src 'self'; media-src 'self' blob:; object-src 'none'; frame-ancestors 'none'"
    )
    if request.is_secure:
        response.headers["Strict-Transport-Security"] = "max-age=31536000; includeSubDomains"
    return response


@app.errorhandler(413)
def request_too_large(_error):
    return jsonify(error="Request is too large."), 413


@app.get("/")
def index():
    return render_template("index.html", languages=languages)


@app.post("/api/translate")
def translate():
    if is_rate_limited("translate"):
        return jsonify(error="Too many translation requests. Please try again later."), 429
    data = request.get_json(silent=True) or {}
    text = str(data.get("text", "")).strip()
    source = data.get("source", "auto")
    target = data.get("target", "es")

    if not text:
        return jsonify(error="Enter some text to translate."), 400
    if len(text) > 5000:
        return jsonify(error="Text must be 5,000 characters or fewer."), 400
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
    except Exception:
        app.logger.exception("Translation service request failed")
        return jsonify(error="Translation service unavailable. Please try again later."), 502


@app.post("/api/speak")
def speak():
    if is_rate_limited("speak"):
        return jsonify(error="Too many audio requests. Please try again later."), 429
    data = request.get_json(silent=True) or {}
    text = str(data.get("text", "")).strip()
    language = data.get("language", "en")

    if not text:
        return jsonify(error="There is no translated text to speak."), 400
    if len(text) > 5000:
        return jsonify(error="Text must be 5,000 characters or fewer."), 400
    if language not in language_codes:
        return jsonify(error="Select a valid language for audio."), 400

    try:
        audio = io.BytesIO()
        gTTS(text=text, lang=language, slow=False).write_to_fp(audio)
        audio.seek(0)
        return send_file(audio, mimetype="audio/mpeg", download_name="translation.mp3")
    except Exception:
        app.logger.exception("Text-to-speech request failed")
        return jsonify(error="Text-to-speech service unavailable. Please try again later."), 502


if __name__ == "__main__":
    app.run(debug=os.getenv("FLASK_DEBUG") == "1")