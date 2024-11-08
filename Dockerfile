# Python image-ini seçirik
FROM python:3.11-slim

# İş qovluğunu təyin edirik
WORKDIR /app

# Layihə fayllarını konteynerə kopyalayırıq
COPY . /app

# Tələb olunan paketləri yükləyirik
RUN pip install --no-cache-dir -r requirements.txt

# Django layihəsini işə salırıq
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
