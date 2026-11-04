const URL = "PASTE_YOUR_MODEL_LINK_HERE/";

let model;

async function loadModel() {
    model = await tmImage.load(URL + "model.json", URL + "metadata.json");
}
loadModel();

document.getElementById("imageUpload").addEventListener("change", function(event) {
    const file = event.target.files[0];
    const img = document.getElementById("preview");
    img.src = URL.createObjectURL(file);
});

async function predict() {
    const img = document.getElementById("preview");

    const prediction = await model.predict(img);

    let maxProb = 0;
    let result = "";

    prediction.forEach(p => {
        if (p.probability > maxProb) {
            maxProb = p.probability;
            result = p.className;
        }
    });

    document.getElementById("result").innerHTML =
        `<h3>Disease: ${result}</h3>` + getSolution(result);
}