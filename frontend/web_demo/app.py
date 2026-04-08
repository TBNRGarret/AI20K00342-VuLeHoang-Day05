import streamlit as st
import requests
import os

st.set_page_config(page_title="Chatbot Tài Xế Xanh SM", layout="wide")

st.title("🚖 Chatbot Tài Xế Xanh SM")
st.markdown("Hệ thống hỗ trợ giải đáp thắc mắc cho tài xế Xanh SM.")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Hỏi tôi về quy định, chính sách..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    try:
        # Gọi Backend API
        response = requests.post(
            "http://localhost:8000/chat",
            json={"message": prompt}
        )
        if response.status_code == 200:
            reply = response.json()["reply"]
        else:
            reply = "Lỗ kết nối đến Backend."
    except Exception as e:
        reply = f"Lỗi: {str(e)}"

    with st.chat_message("assistant"):
        st.markdown(reply)
    st.session_state.messages.append({"role": "assistant", "content": reply})
