# python playground

## About this project

Fun playground that is to be used to test out various scenarios in python.

## Installing dependencies

Note: We assume you are running this in Linux

This project uses [Poetry](https://python-poetry.org/docs/). To install dependencies, run:

Install pyenv first [here](https://github.com/pyenv/pyenv-installer).

```sh
# install python version
pyenv install 3.8.0
# set/activate local python version
pyenv local 3.8.0
# install poetry
pip install poetry
# install poetry settings using pyproject.toml file
poetry install
```

## Format checks

make lint - execute flake8

make black - run black and format files

## Testing

```sh
make unit-test
```

## Running

```sh
make all
```
