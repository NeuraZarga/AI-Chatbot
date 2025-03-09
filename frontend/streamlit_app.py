import streamlit as st
import requests

# URL de notre API FastAPI
API_URL = "http://127.0.0.1:8000/chat"

st.title("🤖 Chatbot IA - Powered by GPT-4")

# Stocker l'historique dans la session Streamlit
if "messages" not in st.session_state:
    st.session_state.messages = []

# Afficher l'historique des messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# Entrée utilisateur
user_input = st.text_input("💬 Votre message :", key="user_input")

if st.button("Envoyer"):
    if user_input:
        # Ajouter le message utilisateur dans l'historique local
        st.session_state.messages.append({"role": "user", "content": user_input})
        
        # Envoyer la requête à notre API FastAPI
        response = requests.post(API_URL, json={"user_input": user_input})
        
        if response.status_code == 200:
            chatbot_response = response.json()["response"]
            
            # Ajouter la réponse du chatbot dans l'historique local
            st.session_state.messages.append({"role": "assistant", "content": chatbot_response})
            
            # Afficher la réponse
            with st.chat_message("assistant"):
                st.write(chatbot_response)
        else:
            st.error("❌ Erreur avec l'API !")
