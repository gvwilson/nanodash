const SIZE = 100;
const GRAY = "#808080";

function hex(num) {
    const hex = num.toString(16);
    return hex.length == 1 ? "0" + hex : hex;
}

async function handleClick() {
    const response = await fetch("http://127.0.0.1:5000/");
    const data = await response.json();
    const color = `#${hex(data["red"])}${hex(data["green"])}${hex(data["blue"])}`;
    const box = document.getElementById(`box`);
    box.setAttribute("fill", color);
}

function drawInitial() {
    const drawing = SVG().addTo("#placeholder").size(SIZE, SIZE);
    drawing.rect(SIZE, SIZE).attr({ fill: GRAY, id: 'box' }).move(0, 0);
}

window.addEventListener("load", drawInitial)
