import streamlit as st
import requests

API_KEY = os.getenv("DIFY_API_KEY")
API_URL = "https://api.dify.ai/v1/chat-messages"

def ask_dify(user_msg):
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "inputs": {},              # must not omit this
        "query": user_msg,
        "user": "user_123"
    }
    response = requests.post(API_URL, headers=headers, json=data)
    if response.status_code == 200:
        result = response.json()
        if "answer" in result:
            return result["answer"]
        else:
            return str(result)
    else:
        return f"Error {response.status_code}: {response.text}"

st.title("Emotional Intelligence Coach Bot")
st.write("Ask me anything about emotional intelligence, stress, and empathy!")

if "history" not in st.session_state:
    st.session_state["history"] = []

user_msg = st.text_input("You:", "")

if user_msg:
    st.session_state["history"].append(("You", user_msg))
    bot_response = ask_dify(user_msg)
    st.session_state["history"].append(("Bot", bot_response))

for speaker, msg in st.session_state["history"]:
    st.markdown(f"**{speaker}:** {msg}")
