# Python image-ini seçirik
FROM python:3.11-slim

# İş qovluğunu təyin edirik
WORKDIR /app

# Layihə fayllarını konteynerə kopyalayırıq
COPY . /app

# Tələb olunan paketləri yükləyirik
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

