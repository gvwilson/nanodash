include tutorials.mk

## build: build website
build:
	ark build
	touch docs/.nojekyll

## serve: serve website
serve:
	ark serve

## lint: check code
lint:
	ruff check ??-*
