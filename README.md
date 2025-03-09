# AI-Chatbot - Powered by GPT-4

AI-Chatbot est un assistant IA basé sur GPT-4, utilisant **FastAPI** pour le backend et **Streamlit** pour l'interface utilisateur.

## Technologies utilisées
- **GPT-4** via OpenAI API
- **FastAPI** pour le backend
- **Streamlit** pour le frontend
- **Docker** pour le déploiement
- **GitHub Actions** pour CI/CD

## Fonctionnalités
- 🔹 Chatbot intelligent avec historique de conversation
- 🔹 Interface web interactive
- 🔹 Mode debug pour afficher les tokens
- 🔹 Optimisation des coûts API OpenAI

## Installation
```bash
git clone https://github.com/NeuraZarga/AI-Chatbot.git
cd AI-Chatbot
pip install -r backend/requirements.txt
streamlit run frontend/streamlit_app.py
