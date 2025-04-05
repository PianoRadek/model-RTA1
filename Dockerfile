# Użyj lekkiego obrazu Pythona
FROM python:3.10-slim

# Ustaw katalog roboczy
WORKDIR /app

# Skopiuj pliki do kontenera
COPY . .

# Zainstaluj zależności
RUN pip install --no-cache-dir -r requirements.txt

# Uruchom aplikację bezpośrednio przez Pythona
CMD ["python", "app.py"]
