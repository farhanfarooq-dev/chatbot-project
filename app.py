import streamlit as st
from openai import OpenAI
import os
from dotenv import load_dotenv
import requests

load_dotenv()

st.title("Hybrid AI Movie Chatbot")

# 🔀 Mode selector
mode = st.radio("Choose mode", ["Ollama (offline)", "OpenAI (online)"])

# 🟢 OpenAI function
def ask_openai(prompt):
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role": "system", "content": "You are a helpful movie assistant."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content

# 🔵 Ollama function
def ask_ollama(prompt):
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "llama3",
            "prompt": f"You are a helpful movie assistant.\nUser: {prompt}",
            "stream": False
        }
    )
    return response.json()["response"]

# 🧾 Input
user_input = st.text_input("Ask anything about movies")

# 🚀 Logic
if user_input:
    try:
        if mode == "OpenAI (online)":
            reply = ask_openai(user_input)
        else:
            reply = ask_ollama(user_input)

        st.write("Bot:", reply)

    except Exception as e:
        st.error(f"Error: {e}")