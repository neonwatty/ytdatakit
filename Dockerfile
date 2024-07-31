# Build stage
FROM python:3.10-slim AS builder

RUN apt-get update && apt-get install -y \
    build-essential \
    software-properties-common \
    ffmpeg \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /home

COPY requirements.txt .

RUN pip3 install --no-cache-dir -r requirements.txt

# Runtime stage
FROM python:3.10-slim

ENV PYTHONPATH=.

WORKDIR /home

COPY --from=builder /usr/local/lib/python3.10/site-packages /usr/local/lib/python3.10/site-packages
COPY --from=builder /usr/local/bin /usr/local/bin
COPY ytdatakit /home/ytdatakit
COPY .streamlit /home/.streamlit

EXPOSE 8501

HEALTHCHECK CMD curl --fail http://localhost:8502/_stcore/health || exit 1

ENTRYPOINT ["streamlit", "run", "/home/ytdatakit/app.py", "--server.port=8502", "--server.address=0.0.0.0"]