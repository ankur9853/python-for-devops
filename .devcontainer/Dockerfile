# Base image with Python 3.11
FROM mcr.microsoft.com/devcontainers/python:1-3.11-bullseye

# Install additional system packages
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    wget \
    git \
    vim \
    nano \
    jq \
    unzip \
    && rm -rf /var/lib/apt/lists/*

# Install AWS CLI v2
RUN curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip" && \
    unzip awscliv2.zip && \
    ./aws/install && \
    rm -rf aws awscliv2.zip

# Set Python environment variables
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=1

# Upgrade pip, setuptools, and wheel
RUN pip install --upgrade pip setuptools wheel

# Install common Python development tools
RUN pip install \
    ipython \
    jupyter \
    pytest \
    black \
    pylint \
    flake8 \
    requests \
    boto3

WORKDIR /workspace
