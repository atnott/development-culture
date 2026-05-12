FROM python:3.14-slim

WORKDIR /app

COPY poetry.lock pyproject.toml ./
RUN pip install poetry && poetry install --only main --no-root

COPY src/app ./app

#poetry run uvicorn src.app.main:app
#--port 8001 --host 127.0.0.1
EXPOSE 8000
CMD [ "poetry", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000" ]