# PROJET DJANGO – Un RAG pour un bot spécialisé en logistique

## 🎯 Objectif du projet

Créer un chatbot capable de répondre aux questions des utilisateurs sur des données liées
aux métiers de la logistique : finance, commerce, juridique, ADR, etc.

---

## 🗄️ Données collectées

J’ai rassemblé des documents PDF à jour (ADR 2025), Incoterms, et codes juridiques (assurance, douane, transport…).

La base de données choisie est PostgreSQL, que je maîtrise bien, avec l’extension pgvector pour gérer les données vectorielles, très utile avec Django.

> **Technos utilisées** : PostgreSQL, Python (Pandas), Django ORM

---

## 📋 Sources et transformations

Documents PDF (officiels)

Tableaux Excel (substances, classes de danger)

Guides pratiques de la douane

---

## 🔄 Pipeline technique avec Langchain, Django et Python

**Ingestion** : extraction du texte via PyMuPDF ou pdfminer.

**Indexation** : requêtes vectorielles avec django-pgvector + PostgreSQL.

> **Technologies utilisées** : Python, Langchain

---

## 🚀 Stack technique

- **Back-end** : Python, Django
- **Base de données** : PostgreSQL
- **Pipeline** : LangChain
- **Frontend** : Django templates, HTML/CSS , Tailwindcss, Daisyui

---

## 📁 Structure du projet (exemple)

CHATBOT_LOG/
├── bot/ # Back-end du bot
├── chatbot_log/ # Config Django
│ ├── settings.py
│ └── urls.py
├── env/ # Environnement virtuel
├── frontend/ # Frontend et templates
│ └── templates/
│ └── frontend/
│ ├── base.html
│ └── index.html
├── Nginx/ # Serveur web (distribution + proxy)
├── register/ # Module d’authentification
│ ├── templates/
│ │ ├── register/login.html
│ │ └── socialaccount/login.html
│ ├── urls.py
│ └── views.py
├── static/ # Fichiers CSS/images
│ ├── src/
│ └── img/
├── .env
├── docker-compose.yml
├── Dockerfile
├── entrypoint.sh
├── manage.py
├── package.json
└── requirements.txt
