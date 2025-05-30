import { convertRequest } from "./requests/convert.js";

document.addEventListener("DOMContentLoaded",async () => {
    const textArea = document.getElementById("text");
    const idiomaSelect = document.getElementById("idioma-select");
    const startAudio = document.getElementById("start-audio");
    const downloadAudio = document.getElementById("download-audio");

    startAudio.addEventListener("click", async () => {
        const text = textArea.value;
        const lang = idiomaSelect.value;

        try {
            const response = await convertRequest(text, lang);

            if (response && response.audio) {
                const audio = new Audio(response.audio);
                await audio.play();
            } else {
                alert("ocorreu um erro ao gerar o áudio!");
            }
        } catch (err) {
            alert(err);
        }
    });
});