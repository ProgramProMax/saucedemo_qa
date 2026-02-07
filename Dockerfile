FROM python:3.10-slim

WORKDIR /app

COPY . .

RUN apt-get update && apt-get install -y \
    wget \
    fonts-liberation \
    libasound2 \
    libatk-bridge2.0-0 \
    libatk1.0-0 \
    libatspi2.0-0 \
    libcups2 \
    libdbus-1-3 \
    libdrm2 \
    libgbm1 \
    libnspr4 \
    libnss3 \
    libxcomposite1 \
    libxdamage1 \
    libxfixes3 \
    libxkbcommon0 \
    libxrandr2 \
    xdg-utils \
    chromium \
    --no-install-recommends \
    && rm -rf /var/lib/apt/lists/*

# Установка Allure
RUN wget https://github.com/allure-framework/allure2/releases/download/2.36.0/allure-2.36.0.tgz \
    && tar -zxvf allure-2.36.0.tgz \
    && ln -s ./allure-2.36.0/bin/allure /usr/bin/allure

RUN pip install --no-cache-dir -r requirements.txt

RUN mkdir -p allure-results

CMD ["pytest", "tests/", "--alluredir=allure-results", "-v"]
