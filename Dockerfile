FROM apache/airflow:2.5.0

# Переключаемся на root для выполнения установки
USER root

# Установка необходимых инструментов для компиляции Python
RUN apt-get update && apt-get install -y \
    wget \
    build-essential \
    libssl-dev \
    zlib1g-dev \
    libncurses5-dev \
    libnss3-dev \
    libsqlite3-dev \
    libreadline-dev \
    libffi-dev \
    curl \
    libbz2-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Установка Python 3.12.1
RUN wget https://www.python.org/ftp/python/3.12.1/Python-3.12.1.tgz \
    && tar -xzf Python-3.12.1.tgz \
    && cd Python-3.12.1 \
    && ./configure --enable-optimizations \
    && make \
    && make install \
    && cd .. \
    && rm -rf Python-3.12.1 Python-3.12.1.tgz

# Переключаемся обратно на airflow пользователя
USER airflow

# Install required Python packages
RUN pip install yfinance mlflow catboost apache-airflow psycopg2-binary
