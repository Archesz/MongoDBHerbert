import streamlit as st
import random
import time
import requests

def send_message(prompt):
    response = requests.post('http://localhost:5000/receber_dados', data={'entrada': prompt})
    return response.text

st.title("Teste Herbert AI")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
    
# Accept user input
if prompt := st.chat_input("Comece a conversa"):
    
    with st.chat_message("user"):
        st.markdown(prompt)
    
    with st.empty():
        st.write("Aguarde um momento, estou processando sua solicitação...")
        bot = send_message(prompt)
        time.sleep(1)  # Simulating a slight delay for better user experience
        st.empty()  # Clear loading message
        
    with st.chat_message("assistant"):
        st.markdown(bot)
    
    # Add user message to chat history
    st.session_state.messages.append({"role": "assistant", "content": bot})
    st.session_state.messages.append({"role": "user", "content": prompt})