import { requestAudio } from "./request.js";

// elements constants
const startAudio = document.getElementById("start-audio");
const downloadAudio = document.getElementById("download-audio");

startAudio.addEventListener("click", async () => {
    const textArea = document.getElementById("text");
    const idiomaSelect = document.getElementById("idioma-select");

    if (!textArea.value) return alert("Você precisa inserir um texto!");

    try {
        await requestAudio(textArea.value, idiomaSelect.value);
        const audio = new Audio(`http://127.0.0.1:8000/audio/audio.mp3?t=${Date.now()}`);
        audio.play();
    } catch (err) {
        console.log(err);
    }
});

downloadAudio.addEventListener("click", async () => {
    // ...
});