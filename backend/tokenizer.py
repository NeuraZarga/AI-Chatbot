import tiktoken
import openai
import json
import os

# Récupération de la key openai
openai.api_key = os.getenv("OPENAI_API_KEY")

# Charger les paramètres depuis un fichier de config
CONFIG_FILE = "config.json"

# Charger la config
def charger_config():
    try:
        with open(CONFIG_FILE, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return { "temperature" : 0.5} # Température par défaut
    
config = charger_config()
print(config["temperature"])

# 🔹 Initialisation du tokenizer OpenAI (GPT-4)
encoding = tiktoken.get_encoding("cl100k_base")

# 🔹 Fonction pour mesurer le nombre de tokens
def compter_tokens(texte):
    return len(encoding.encode(texte))

# 🔹 Fonction de réduction des tokens
def optimiser_texte(texte):
    try:
        response = openai.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "Résume ce texte de manière concise mais claire."},
                {"role": "user", "content": texte}
            ],
            max_tokens=30,
            temperature=config["temperature"]  # Ajustable depuis config.json
        )
        texte_reduit = response.choices[0].message.content
        
        # Vérification si la phrase est coupée
        if texte_reduit[-1] not in ".!?":
            texte_reduit += "..."

        return texte_reduit
    except Exception as e:
        print("Erreur avec OpenAI :", e)
        return texte  # Retourne le texte original en cas d'erreur

# 🔹 TEST : Vérifier que tout fonctionne bien
if __name__ == "__main__":
    texte_test = "Bonjour frérot, on optimise la tokenization pour notre chatbot afin de réduire les coûts !"
    
    print("\n🔹 Texte original :", texte_test)
    print(f"Nombre de tokens : {compter_tokens(texte_test)}")
    
    texte_optimise = optimiser_texte(texte_test)
    print("\n🔹 Texte optimisé :", texte_optimise)
    print(f"Nombre de tokens après optimisation : {compter_tokens(texte_optimise)}")
