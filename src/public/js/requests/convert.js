export async function convertRequest(text, lang) {
    try {
        const request = await fetch("http://127.0.0.1:8000/convert", {
            method: "POST",
            headers: {"Content-Type": "application/json"},
            body: JSON.stringify({ text: text, lang: lang })
        });

        if (!request.ok) throw new Error(`${request.status} - ${request.statusText}`);
        
        const dataJson = await request.json();
        return dataJson;
    } catch (err) {
        console.error(err);
    }
};