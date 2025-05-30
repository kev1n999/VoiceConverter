import os 
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from gtts import gTTS 
from pydantic import BaseModel
from uuid import uuid4

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

if not os.path.exists("audios"):
    os.makedirs("audios")

app.mount("/audios", StaticFiles(directory="audios"), name="audios")

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
        filename = f"{uuid4()}.mp3"
        path = f"audios/{filename}"
        
        tts = gTTS(bodyRequest.text, lang=bodyRequest.lang)
        tts.save(path)
        return { "status": 200, f"audio": f"http://127.0.0.1:8000/audios/{filename}" }
    except Exception as err:
       return { "status": "error", "message": str(err) }
        