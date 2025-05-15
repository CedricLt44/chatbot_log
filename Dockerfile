# Use the official Python runtime image
FROM python:3.13-slim

# Variables d'environnement pour un comportement cohérent
ENV PYTHONUNBUFFERED=1 \
  PYTHONDONTWRITEBYTECODE=1 \
  VIRTUAL_ENV=/env \
  PATH="/env/bin:$PATH"


# Mise à jour système + installation Node.js + nettoyage en une seule commande
RUN apt-get update && apt-get upgrade -y && \
  apt-get install -y curl gnupg postgresql-client && \
  curl -fsSL https://deb.nodesource.com/setup_18.x | bash - && \
  apt-get install -y nodejs && \
  apt-get clean && rm -rf /var/lib/apt/lists/*

# Définit le répertoire de travail dans le conteneur
# Créer le répertoire et définir le workdir en une seule étape
WORKDIR /app

# Configurer l'environnement virtuel et installer les dépendancesd
COPY requirements.txt .

RUN python -m venv /env \
  && /env/bin/pip install --upgrade pip \
  && /env/bin/pip install -r requirements.txt

# Copier le reste du code de l'application
COPY . /app

COPY .env /app/.env

# Rendre le script d'entrée exécutable
RUN chmod +x entrypoint.sh

# Définir la commande par défaut
CMD ["bash", "/app/entrypoint.sh"]