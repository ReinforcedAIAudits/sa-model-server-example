FROM python:3.11-slim

RUN mkdir /app

WORKDIR /app

RUN python -c "import urllib.request; urllib.request.urlretrieve('https://huggingface.co/bartowski/Phi-3.5-mini-instruct-GGUF/resolve/main/Phi-3.5-mini-instruct-Q6_K_L.gguf', '/app/Phi-3.5-mini-instruct-Q6_K_L.gguf')"

RUN apt-get update && apt-get install build-essential -y

RUN pip install llama-cpp-python flask gunicorn

ADD main.py .

CMD ["gunicorn", "--workers", "1", "--threads", "1", "--bind", "0.0.0.0:5000", "--access-logfile", "-", "--error-logfile", "-", "main:app"]