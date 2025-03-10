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

## Contribution
Toute contribution est la bienvenue ! Pour proposer des améliorations :
1. Forkez ce repo
2. Créez une branche (`feature-nouvelle-fonctionnalité`)
3. Faites vos modifications et committez (`git commit -m "Ajout d'une nouvelle feature"`)
4. Poussez votre branche (`git push origin feature-nouvelle-fonctionnalité`)
5. Faites une pull request !


## 📌 Installation

```bash
git clone https://github.com/NeuraZarga/AI-Chatbot.git
cd AI-Chatbot

# 1️⃣ Créer et activer un environnement virtuel
python3 -m venv venv
source venv/bin/activate

# 2️⃣ Installer les dépendances
pip install -r requirements.txt

# 3️⃣ Définir la clé API OpenAI (Remplacer avec ta clé)
export OPENAI_API_KEY="ta_clé"

# 4️⃣ Lancer l'API (Backend)
uvicorn backend.api:app --host 0.0.0.0 --port 8000 --reload  

# 5️⃣ Lancer l'interface (Frontend)
streamlit run frontend/streamlit_app.py


