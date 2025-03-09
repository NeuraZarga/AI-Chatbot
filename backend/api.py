from fastapi import FastAPI
import openai
import json
import os
from pydantic import BaseModel
from tokenizer import compter_tokens

# Activation du mode debug
DEBUG_MODE = True  # Passer à False si on ne veut pas afficher les logs

# Charger l'historique depuis un fichier JSON
HISTORIQUE_FILE = "historique.json"

# Initialisation de FastAPI
app = FastAPI()

# 🔹 Définir la clé API OpenAI
openai.api_key = os.getenv("OPENAI_API_KEY")

class ChatRequest(BaseModel):
    user_input: str

# Charger l'historique
def charger_historique():
    try:
        with open(HISTORIQUE_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

# Sauvegarder l'historique
def sauvegarder_historique(historique):
    with open(HISTORIQUE_FILE, "w") as f:
        json.dump(historique, f, indent=4)


@app.get("/")
def welcome_to_the_chatbot_api():
    return { "message" : "Welcome Bro, on lache rien !!!"}


@app.post("/test_chat")
async def chat(request: ChatRequest):
    return {"response": f"Tu as dit : {request.user_input}"}


@app.post("/chat")
async def chat(request: ChatRequest):
    historique = charger_historique()

     # 🔍 DEBUG : Affichage de l'historique avant l'ajout du message
    if DEBUG_MODE:
        print("\ Historique AVANT :", historique)
        print(f"Tokens actuels dans l'historique : {compter_tokens(str(historique))}")

    # Ajout du message utilisateur dans l'historique
    historique.append({"role": "user", "content": request.user_input})
    
    # Appel à OpenAI API
    response = openai.chat.completions.create(
        model="gpt-4",
        messages=historique,
        max_tokens=300,
        temperature=0.7
    )

    # Récupérer la réponse
    chatbot_response = response.choices[0].message.content

    # Ajouter la réponse du chatbot dans l'historique
    historique.append({"role": "assistant", "content": chatbot_response})
    sauvegarder_historique(historique)

    # 🔍 DEBUG : Affichage de la requête envoyée à OpenAI
    if DEBUG_MODE:
        print("\n Requête envoyée à OpenAI :")
        print(json.dumps(historique, indent=4))
        print(f"Tokens générés par OpenAI : {compter_tokens(chatbot_response)}")
        print(f"Tokens après mise à jour : {compter_tokens(str(historique))}")
        print("Réponse générée :", chatbot_response)

    return {"response": chatbot_response}
