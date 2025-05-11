import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from gtts import gTTS 
from pydantic import BaseModel

app = FastAPI()

app.mount("/audio", StaticFiles(directory=os.path.join(os.path.dirname(__file__), "audio")), name="audio")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:5500"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class BodyRequest(BaseModel):
    text: str
    lang: str 
    
@app.get("/")
def home():
    return {
        "status": 200,
    }
    
@app.post("/convert")
def convert_text_to_voice(bodyRequest: BodyRequest):
    try:
        tts = gTTS(bodyRequest.text, lang=bodyRequest.lang)
        audio_dir = os.path.join(os.path.dirname(__file__), "audio")
        
        tts.save(os.path.join(audio_dir, "audio.mp3"))
        return { "status": 200 }
    except Exception as err:
        print(err)