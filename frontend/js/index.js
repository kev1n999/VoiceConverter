import { requestAudio } from "./request.js";

// elements constants
const textArea = document.getElementById("text");
const idiomaSelect = document.getElementById("idioma-select");
const startAudio = document.getElementById("start-audio");
const downloadAudio = document.getElementById("download-audio");

startAudio.addEventListener("click", async () => {
    const req = await requestAudio(textArea.value, idiomaSelect.value);

    alert(req);
});

downloadAudio.addEventListener("click", async () => {
    // ...
});