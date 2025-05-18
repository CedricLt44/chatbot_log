import os
from urllib.parse import quote_plus
from dotenv import load_dotenv

# Charger les variables d'environnement depuis .env
load_dotenv()

# Récupération des variables
user = os.getenv("POSTGRES_USER")
password = quote_plus(os.getenv("POSTGRES_PASSWORD"))  # encodage sécurisé
host = os.getenv("POSTGRES_HOST")
port = os.getenv("POSTGRES_PORT")
dbname = os.getenv("POSTGRES_DB")

# Construction de la chaîne de connexion
connection_string = f"postgresql+psycopg2://{user}:{password}@{host}:{port}/{dbname}"

# Affichage pour vérification
print("Chaîne de connexion :", connection_string)
import psycopg2

try:
    conn = psycopg2.connect(
        dbname=dbname,
        user=user,
        password=os.getenv("POSTGRES_PASSWORD"),
        host=host,
        port=port
    )
    print("✅ Connexion à PostgreSQL réussie.")
    conn.close()
except Exception as e:
    print("❌ Erreur de connexion :", e)