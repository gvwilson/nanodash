# Contributing

Contributions are very welcome.  Please file issues or submit pull
requests in our GitHub repository.  All contributors will be
acknowledged, but must abide by our Code of Conduct.

## Usage

-   Run `make` in the root directory or any subdirectory containing an `index.md` file to see available commands.

## Site Structure

-   `README.md`: overview
-   `LICENSE.md`: content license
-   `CODE_OF_CONDUCT.md`: code of conduct
-   `CONTRIBUTING.md`: this contributors' guide
-   `Makefile`: reusable commands
-   `index.md`: home page
-   `*_.md`: Jekyll wrappers for license, contributors' guide, and code of conduct
-   `requirements.txt`: Python package list
-   `src/`: source code (one sub-directory per tutorial episode)
    -   `src/00-intro`: introduction
    -   `src/01-manual`: hand-written JavaScript and Python
-   `tutorials.mk`: shared reusable commands
