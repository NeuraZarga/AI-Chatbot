import openai
import json
import os
from historique import get_historique, ajouter_message
from tokenizer import compter_tokens


# 🔹 Charger la config
CONFIG_FILE = "config.json"

def charger_config():
    try:
        with open(CONFIG_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {"temperature": 0.5}  # Température par défaut

config = charger_config()


# 🔹 Définir la clé API OpenAI
openai.api_key = os.getenv("OPENAI_API_KEY")

# 🔹 Fonction principale du chatbot
def repondre(message):
    # 🔹 Ajouter le message de l'utilisateur à l'historique
    ajouter_message("user", message)

    # 🔹 Récupérer l'historique formaté
    historique = get_historique()

    # 🔹 Vérifier le nombre total de tokens dans l'historique
    tokens_total = sum(compter_tokens(msg["content"]) for msg in historique)
    print(f"\n Tokens actuels dans l'historique : {tokens_total}")

    # 🔹 Vérifier le nombre total de tokens pour éviter de dépasser la limite OpenAI
    tokens_total = sum(compter_tokens(msg["content"]) for msg in historique)
    if tokens_total > 1700:  # GPT-4 Turbo a une limite élevée, on garde 3000 tokens max
        print("\n Trop de tokens, on va tronquer l'historique...")
        historique = historique[-10:]  # 🔹 On garde les 10 derniers échanges

    try:
        # 🔹 Appel à l'API OpenAI
        response = openai.chat.completions.create(
            model="gpt-4",
            messages=historique,
            max_tokens=300,
            temperature=config["temperature"]
        )

        # 🔹 Récupérer la réponse générée
        reponse_chatbot = response.choices[0].message.content

        # 🔹 Calcul des tokens générés
        tokens_generes = compter_tokens(reponse_chatbot)
        print(f"\n Tokens générés par OpenAI : {tokens_generes}")

        # 🔹 Ajouter la réponse à l'historique
        ajouter_message("assistant", reponse_chatbot)

        return reponse_chatbot

    except Exception as e:
        print("Erreur avec OpenAI :", e)
        return "Je rencontre un problème technique. Réessaie plus tard."
    


# 🔹 TEST : Simuler une conversation
if __name__ == "__main__":
    while True:
        message = input("\n💬 Toi : ")
        if message.lower() in ["exit", "quit", "stop"]:
            print("Fin de la session.")
            break
        
        reponse = repondre(message)
        print(f"\n Chatbot : {reponse}")
