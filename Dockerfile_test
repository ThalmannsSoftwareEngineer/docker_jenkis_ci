# Verwende das offizielle Python-Image als Basis
FROM python:3.9

# Installiere Git
RUN apt-get update && apt-get install -y git

# Setze das Arbeitsverzeichnis im Container
WORKDIR /app

# Kopiere die Anwendungsdateien in das Arbeitsverzeichnis
COPY . /app

# Führe ein Kommando aus, um die erforderlichen Python-Pakete zu installieren
RUN apt-get update
RUN apt-get install -y podman git python3-pip
RUN python3 -m pip install git-review podman-compose
# Klonen des Git-Repositorys
RUN git clone https://opendev.org/zuul/zuul

# Führe das Python-Skript aus
# CMD ["python", "app.py"]
