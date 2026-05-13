FROM ubuntu:22.04

LABEL author="shashkov777"

WORKDIR /app

RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    && rm -rf /var/lib/apt/lists/*

COPY . .

RUN pip3 install requests

CMD ["python3", "script.py"]
