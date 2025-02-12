# Dockerfile for Python client

FROM python:3.9-slim

WORKDIR /app

# COPY the python script

COPY ./src/quote_client.py .

# Run the client when the container starts
CMD ["python", "quote_client.py"]