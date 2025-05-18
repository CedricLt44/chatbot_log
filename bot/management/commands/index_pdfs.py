import os
import pdfplumber
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import PGVector
from langchain.text_splitter import CharacterTextSplitter
from urllib.parse import quote_plus
# === Configuration de la base vectorielle PostgreSQL (ex : pgvector) ===
collection_name = "pdf_collection"

# Récupération des variables
user = os.getenv("POSTGRES_USER")
password = quote_plus(os.getenv("POSTGRES_PASSWORD"))  # encodage sécurisé
host = os.getenv("POSTGRES_HOST")
port = os.getenv("POSTGRES_PORT")
dbname = os.getenv("POSTGRES_DB")

# Construction de la chaîne de connexion
connection_string = f"postgresql+psycopg2://{user}:{password}@{host}:{port}/{dbname}"

# === Initialisation des embeddings avec HuggingFace (modèle local) ===
embedding = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# === Fonction de traitement PDF ===
def load_and_split_pdfs(pdf_dir):
    all_chunks = []
    splitter = CharacterTextSplitter(
        separator="\n",
        chunk_size=1000,
        chunk_overlap=200
    )

    for filename in os.listdir(pdf_dir):
        if filename.endswith(".pdf"):
            path = os.path.join(pdf_dir, filename)
            print(f"Traitement : {filename}")
            with pdfplumber.open(path) as pdf:
                full_text = ""
                for page in pdf.pages:
                    try:
                        full_text += page.extract_text() + "\n"
                    except Exception as e:
                        print(f"Erreur extraction page : {e}")
                        continue

                chunks = splitter.create_documents([full_text], metadatas=[{"source": filename}])
                all_chunks.extend(chunks)

    return all_chunks

# === Point d'entrée Django ===
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = "Indexe les fichiers PDF en base vectorielle"

    def handle(self, *args, **options):
        pdf_dir = "F:/APPLICATION/chatbot_log/bot/doc_pdf"
        print("Chargement et découpage des PDF...")
        all_chunks = load_and_split_pdfs(pdf_dir)

        print(f"Nombre de documents à vectoriser : {len(all_chunks)}")

        # === Indexation dans la base vectorielle ===

        PGVector.from_documents(
            documents=all_chunks,
            embedding=embedding,
            collection_name=collection_name,
            connection_string=connection_string
        )

        print("✅ Indexation terminée avec succès.")