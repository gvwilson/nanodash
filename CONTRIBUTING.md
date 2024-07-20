# Contributing

Contributions are very welcome.  Please file issues or submit pull
requests in our GitHub repository.  All contributors will be
acknowledged, but must abide by our Code of Conduct.

## Usage

To build or preview this site:
-   Create a virtual environment using Python 3.12
-   Install requirements with `pip install -r requirements.txt`
-   Run `make build` to build the website into `./docs`
-   Run `make serve` to preview the website

## Site Structure

-   `README.md`: overview
-   `LICENSE.md`: content license
-   `CODE_OF_CONDUCT.md`: code of conduct
-   `CONTRIBUTING.md`: this contributors' guide
-   `requirements.txt`: Python package list
    -   Relies on `lib/amw/requirements.txt` for Ark template
-   `Makefile`: reusable commands
-   `tutorials.mk`: shared reusable commands
-   `lib/amw/*`: Ark template and extensions
-   `src/`: source code (one sub-directory per tutorial episode)
    -   `src/index.md`: home page
    -   `src/00-intro/*`: introduction
    -   `src/01-manual/*`: hand-written JavaScript and Python
    -   `src/02-dynamic/*`: loading content dynamically
