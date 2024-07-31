FROM python:3.10-slim

RUN apt-get update && apt-get install -y \
    build-essential \
    software-properties-common \
    ffmpeg \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /home

ENV PYTHONPATH=.

COPY requirements.txt /home/requirements.txt
COPY ytdatakit /home/ytdatakit
COPY .streamlit /home/.streamlit
RUN pip3 install -r /home/requirements.txt

EXPOSE 8502

HEALTHCHECK CMD curl --fail http://localhost:8502/_stcore/health || exit 1

ENTRYPOINT ["streamlit", "run", "/home/ytdatakit/app.py", "--server.port=8502", "--server.address=0.0.0.0"]