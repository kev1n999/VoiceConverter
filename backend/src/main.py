import os 
from flask import Flask, jsonify, request 
from flask_cors import CORS 
from gtts import gTTS

app = Flask(__name__)
CORS(app)

@app.get("/")
def home():
    return "Funcionando!"

@app.route("/converter", methods=["POST"])
def convert_text_to_voice():
    data = request.get_json()
    text = data.get("text")
    lang = data.get("lang")
    
    tts = gTTS(text, lang=lang)
    tts.save("audio.mp3")
    return jsonify({
        "success": "true",
        "data": {
            "text": text,
            "lang": lang 
        }
    })    
    
if __name__ == "__main__":
    app.run(debug=True)