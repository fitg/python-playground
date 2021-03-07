FROM hub.docker.zoopla.it/library/python:3.8-slim AS buildbase

WORKDIR /opt

COPY pyproject.toml poetry.lock ./

# Install prerequisites
RUN pip install poetry && apt-get update && apt-get install -y make &&  \
    poetry install --no-root

RUN poetry config virtualenvs.create false && poetry install --no-root --no-dev

COPY src/ ./src

CMD ["poetry", "run", "start_app"]
