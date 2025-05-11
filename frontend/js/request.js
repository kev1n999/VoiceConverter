export async function requestAudio(text, lang) {
    try {
        const request = await fetch("http://127.0.0.1:8000/convert", 
            {
                method: "POST",
                headers: {"Content-Type": "application/json"},
                body: JSON.stringify({
                    text: text,
                    lang: lang 
                })
            }
        )

        const response = await request.json();

        if (request.ok) {
            return response; 
        }

        return response;
    } catch (err) {
        alert(err);
    }
};