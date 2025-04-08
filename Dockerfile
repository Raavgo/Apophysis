FROM python:3.13-slim

# Install curl
RUN apt-get update && apt-get install -y curl

# Install poetry
RUN curl -sSL https://install.python-poetry.org | python3 -
ENV PATH="/root/.local/bin:$PATH"

# Set the working directory inside the container
WORKDIR /app

# Copy all files into the container
COPY . /app/

# Ensure Poetry uses Python 3.13 version
RUN poetry env use python3.13

# Install dependencies with poetry
RUN poetry install --no-root

# CMD