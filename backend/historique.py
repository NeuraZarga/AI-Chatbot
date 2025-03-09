import json
from tokenizer import compter_tokens, optimiser_texte

# 🔹 Fichier où on stocke l'historique (simule une mémoire)
HISTORIQUE_FILE = "data/historique.json"

# 🔹 Charge l'historique des conversations
def charger_historique():
    try:
        with open(HISTORIQUE_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

# 🔹 Sauvegarde l'historique des conversations
def sauvegarder_historique(historique):
    with open(HISTORIQUE_FILE, "w") as f:
        json.dump(historique, f, indent=4)

# 🔹 Ajoute un message à l'historique
def ajouter_message(role, message):
    historique = charger_historique()
    historique.append({"role": role, "content": message})

    # Vérifie la taille de l'historique (on garde max 2000 tokens pour GPT-4 Turbo)
    tokens_total = sum(compter_tokens(msg["content"]) for msg in historique)
    while tokens_total > 2000:  # On réduit les anciens messages si on dépasse
        historique[1]["content"] = optimiser_texte(historique[1]["content"])  # 🔹 Compression intelligente
        tokens_total = sum(compter_tokens(msg["content"]) for msg in historique)

    sauvegarder_historique(historique)

# 🔹 Récupère l'historique formaté pour OpenAI
def get_historique():
    return charger_historique()

# 🔹 TEST : Vérifier que la mémoire fonctionne bien
if __name__ == "__main__":
    ajouter_message("user", "Salut chatbot, comment vas-tu ?")
    ajouter_message("assistant", "Salut ! Je vais bien, merci. Comment puis-je t'aider ?")

    print("\n🔹 Historique actuel :")
    print(json.dumps(get_historique(), indent=4))
