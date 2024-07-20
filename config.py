slug = "nanodash"
title = "Nanodash"
repo = f"https://github.com/gvwilson/{slug}"
authors = [
    {"name": "Martha Cryan", "email": "martha.cryan@plot.ly"},
    {"name": "Emily Kellison-Lim", "email": "emily@plot.ly"},
    {"name": "Greg Wilson", "email": "greg.wilson@plot.ly"},
]

lang = "en"
theme = "amw"
src_dir = "src"
out_dir = "docs"
extension = "/"
exclude = set()

markdown_settings = {
    "extensions": [
        "markdown.extensions.extra",
        "markdown.extensions.smarty",
        "pymdownx.superfences",
    ]
}
