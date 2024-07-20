include tutorials.mk

## build: build website with Jekyll
build:
	jekyll build

## serve: serve website with Jekyll
serve:
	jekyll serve

## lint: check code
lint:
	ruff check ??-*
