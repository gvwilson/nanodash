const SIZE = 100;
const GRAY = "#808080";

function rand() {
    return Math.floor(Math.random() * 256);
}

function hex(num) {
    const hex = num.toString(16);
    return hex.length == 1 ? "0" + hex : hex;
}

function handleClick() {
    const red = rand(), green = rand(), blue = rand();
    const color = `#${hex(red)}${hex(green)}${hex(blue)}`;
    const box = document.getElementById(`box`);
    box.setAttribute("fill", color);
}

function drawInitial() {
    const drawing = SVG().addTo("#placeholder").size(SIZE, SIZE);
    drawing.rect(SIZE, SIZE).attr({ fill: GRAY, id: 'box' }).move(0, 0);
}

window.addEventListener("load", drawInitial)
