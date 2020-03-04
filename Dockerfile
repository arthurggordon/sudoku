FROM python:3.8.2 as base
ENV PYTHONUNBUFFERED 1

WORKDIR /app
RUN pip install pytest


FROM base as debug
# Used for format, lint and debugging
RUN pip install black
RUN pip install flake8
RUN pip install mypy


FROM base as release
COPY ./src .
ENTRYPOINT [ "python3", "main.py"]