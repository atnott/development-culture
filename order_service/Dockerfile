FROM python:3.14-slim

WORKDIR /app

COPY poetry.lock pyproject.toml ./
RUN pip install poetry && poetry install --only main --no-root

COPY src/app ./app

EXPOSE 8000
CMD ["poetry", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]