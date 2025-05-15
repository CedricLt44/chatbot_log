#!/bin/bash

# Arrêter le script en cas d'erreur
set -e

# Attendre que PostgreSQL soit prêt
until pg_isready -h $POSTGRES_HOST -p $POSTGRES_PORT -U $POSTGRES_USER; do
  echo "Attente de PostgreSQL..."
  sleep 2
done

# Activer l'environnement virtuel si tu en as un dans /env (sinon supprime cette ligne)
if [ -f /env/bin/activate ]; then
  source /env/bin/activate
fi

# Créer les migrations (optionnel, si tu préfères automatiser)
python manage.py makemigrations
# Appliquer les migrations
python manage.py migrate

# Collecter les fichiers statiques (pour que Nginx puisse les servir)
echo "Collect static files"
python manage.py collectstatic --noinput

# Démarrer le serveur Django
echo "Starting Django server..."
exec python manage.py runserver 0.0.0.0:8000
