import streamlit as st
from openai import OpenAI
import os
from dotenv import load_dotenv
import requests

load_dotenv()

st.title("💬 Hybrid AI Chatbot by Farhan")

with st.sidebar:
    st.header("⚙️ Settings")

    mode = st.radio(
        "Choose mode",
        ["Ollama (offline)", "OpenAI (online)"]
    )

    if st.button("🧹 Clear Chat"):
        st.session_state.messages = []
        st.rerun()

st.caption(f"Mode: {mode}")

if "messages" not in st.session_state:
    st.session_state.messages = []

def ask_openai(messages):
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=messages
    )
    reply = response.choices[0].message.content
    return "Farhan says: " + reply

def ask_ollama(messages):
    prompt = ""
    for msg in messages:
        role = "User" if msg["role"] == "user" else "Assistant"
        content = msg["content"].replace("Farhan says: ", "")
        prompt += f"{role}: {content}\n"

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "llama3",
            "prompt": prompt,
            "stream": False
        }
    )

    reply = response.json()["response"]
    return "Farhan says: " + reply

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

user_input = st.chat_input("Type your message...")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})

    with st.chat_message("user"):
        st.write(user_input)

    if mode == "OpenAI (online)":
        reply = ask_openai(st.session_state.messages)
    else:
        reply = ask_ollama(st.session_state.messages)

    st.session_state.messages.append({"role": "assistant", "content": reply})

    with st.chat_message("assistant"):
        st.write(reply)