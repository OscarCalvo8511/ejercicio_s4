
import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="Chat IA", page_icon="🤖")

st.title("🤖 Chat con Gemini")
st.markdown("Una app sencilla para conversar con Gemini.")

# Sidebar para configuración
with st.sidebar:
    st.header("⚙️ Configuración")
    api_key = st.text_input("API Key de Gemini", type="password")
    temperatura = st.slider("Temperatura", 0.0, 1.0, 0.7)
    st.markdown("---")
    st.markdown("[Obtener API Key](https://aistudio.google.com/apikey)")

# Inicializar historial
if "mensajes" not in st.session_state:
    st.session_state.mensajes = []

# Mostrar historial
for msg in st.session_state.mensajes:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# Input del usuario
if prompt := st.chat_input("Escribe tu mensaje..."):
    # Mostrar mensaje del usuario
    with st.chat_message("user"):
        st.write(prompt)
    st.session_state.mensajes.append({"role": "user", "content": prompt})

    # Generar respuesta
    if api_key:
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel("gemini-2.5-flash")
        response = model.generate_content(
            prompt,
            generation_config=genai.GenerationConfig(temperature=temperatura)
        )
        respuesta = response.text
    else:
        respuesta = "⚠️ Añade tu API Key de Gemini en la barra lateral."

    # Mostrar respuesta
    with st.chat_message("assistant"):
        st.write(respuesta)
    st.session_state.mensajes.append({"role": "assistant", "content": respuesta})
