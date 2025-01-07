FROM python:3.10-slim

ARG DEBIAN_FRONTEND=noninteractive


RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx \
    libglib2.0-0 \
    libsm6 \
    libxext6 \
    libxrender-dev \
    libx11-6 \
    tzdata \
    libgl1-mesa-dev \
    tk \
    && rm -rf /var/lib/apt/lists/*


WORKDIR /app


COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

CMD ["bash"]
