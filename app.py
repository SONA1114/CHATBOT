import streamlit as st
import google.generativeai as genai

genai.configure(api_key="AIzaSyDrHkTUfSoDByVX_emFWSEsQLGkqh6sTkU")

model = genai.GenerativeModel("models/gemini-2.5-flash")

st.title("🤖 Gemini Chatbot")

if "chat" not in st.session_state:
    st.session_state.chat = model.start_chat(history=[])

for msg in st.session_state.chat.history:
    role = "You" if msg.role == "user" else "Gemini"
    st.markdown(f"**{role}:** {msg.parts[0].text}")

prompt = st.text_input("Say something")

if st.button("Send") and prompt:
    st.session_state.chat.send_message(prompt)
    st.rerun()
