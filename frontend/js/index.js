// elements constants
const textArea = document.getElementById("text");
const idiomaSelect = document.getElementById("idioma-select");
const startAudio = document.getElementById("start-audio");
const downloadAudio = document.getElementById("download-audio");

startAudio.addEventListener("click", () => {
    fetch("http://127.0.0.1:50000/converter", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({ text: textArea.value, lang: idiomaSelect.value }) 
    })
    .then(r => r.text())
    .then(r => alert(r))
    .catch(err => alert(err));
});