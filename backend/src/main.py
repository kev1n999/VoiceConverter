from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from gtts import gTTS 
from pydantic import BaseModel

app = FastAPI()

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
        tts.save("audio.mp3")
        return { "status": 200 }
    except Exception as err:
        print(err)