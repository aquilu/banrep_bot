# **app.py**

# Importando las librerías necesarias
import time
import streamlit as st
from utils import load_chain

# Imagen personalizada para el icono de la app y el avatar del asistente
company_logo = 'https://d1b4gd4m8561gs.cloudfront.net/sites/default/files/favicon.ico'

# Configurando la página de Streamlit
st.set_page_config(
    page_title="Asistente virtual sobre El Banco de la República: antecedentes, evolución y estructura",
    page_icon=company_logo
)

# Inicializando la cadena LLM
chain = load_chain()

# Inicializando el historial del chat
if 'messages' not in st.session_state:
    # Comenzando con el primer mensaje del asistente
    st.session_state['messages'] = [{"role": "assistant", 
                                  "content": "Hola humano! Soy Muisca, la IA que te asiste sobre la historia Banco de la República. ¿Cómo puedo ayudarte hoy?"}]

# Mostrando mensajes del chat desde el historial en cada re-ejecución de la app
# Avatar personalizado para el asistente, avatar predeterminado para el usuario
for message in st.session_state.messages:
    if message["role"] == 'assistant':
        with st.chat_message(message["role"], avatar=company_logo):
            st.markdown(message["content"])
    else:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

# Lógica del chat
if query := st.chat_input("Pregúntame cualquier cosa"):  # Cambiado a español
    # Agregar mensaje del usuario al historial del chat
    st.session_state.messages.append({"role": "user", "content": query})
    # Mostrar mensaje del usuario en el contenedor del chat
    with st.chat_message("user"):
        st.markdown(query)

    with st.chat_message("assistant", avatar=company_logo):
        message_placeholder = st.empty()
        # Enviar la pregunta del usuario a nuestra cadena
        result = chain({"question": query})
        response = result['answer']
        full_response = ""

        # Simular flujo de respuesta con milisegundos de retraso
        for chunk in response.split():
            full_response += chunk + " "
            time.sleep(0.05)
            # Agregar un cursor parpadeante para simular la escritura
            message_placeholder.markdown(full_response + "▌")
        message_placeholder.markdown(full_response)

    # Agregar mensaje del asistente al historial del chat
    st.session_state.messages.append({"role": "assistant", "content": response})
