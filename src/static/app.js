document.getElementById('generate-btn').addEventListener('click', async () => {
    const choices = ["Camisa blanca", "Pantalón negro"]; // Simula elecciones
    const response = await fetch('/generate', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ choices })
    });
    const data = await response.json();
    document.getElementById('result').innerHTML = `<img src="${data.image_url}" alt="Outfit generado">`;
});
