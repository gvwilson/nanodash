slug = "nanodash"
title = "Nanodash"
repo = f"https://github.com/gvwilson/{slug}"
authors = [
    {"name": "Martha Cryan", "email": "martha.cryan@plot.ly"},
    {"name": "Emily Kellison-Lim", "email": "emily@plot.ly"},
    {"name": "Greg Wilson", "email": "greg.wilson@plot.ly"},
]
copy = [
    "*.html",
    "*.js",
    "*.json",
    "*.out",
    "*.png",
    "*.py",
    "*.sh",
    "*.svg",
]

lang = "en"
theme = "amw"
src_dir = "src"
out_dir = "docs"
extension = "/"

markdown_settings = {
    "extensions": [
        "markdown.extensions.extra",
        "markdown.extensions.smarty",
        "pymdownx.superfences",
    ]
}
