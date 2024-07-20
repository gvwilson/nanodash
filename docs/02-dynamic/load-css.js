async function handleClick() {
    const response = await fetch("http://127.0.0.1:5000/");
    const data = await response.text();
    const style = document.createElement("style");
    style.setAttribute("type", "text/css");
    style.textContent = data;
    document.getElementsByTagName("head")[0].appendChild(style);
}
