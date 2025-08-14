FROM python:3.12-slim AS build
RUN apt-get update && apt-get install -y build-essential uvicorn
RUN pip install --no-cache-dir poetry
WORKDIR /app
COPY pyproject.toml poetry.lock ./
RUN poetry install --no-root --only main
COPY . .
CMD ["poetry", "run", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
