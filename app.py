import streamlit as st
import openai

st.set_page_config(page_title="Parker: Sahabat Penyemangat", layout="centered")

st.title("🧡 Parker – Sahabat Penyemangat Kamu")

if "messages" not in st.session_state:
    st.session_state.messages = []

# Masukkan API key pengguna
api_key = st.text_input("Masukkan OpenAI API key kamu:", type="password")
if not api_key:
    st.warning("🔒 Masukkan API key untuk mulai ngobrol dengan Parker.")
    st.stop()

openai.api_key = api_key

# Tampilkan riwayat chat
for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.markdown(f"**Kamu:** {msg['content']}")
    else:
        st.markdown(f"**Parker:** {msg['content']}")

# Input chat dari pengguna
user_input = st.text_input("Kamu:", key="input")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    
    with st.spinner("Parker sedang mikir..."):
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "Kamu adalah sahabat AI bernama Parker. Kamu selalu menyemangati, suportif, ramah, dan bikin senang."},
                    *st.session_state.messages
                ]
            )
            reply = response.choices[0].message["content"]
        except Exception as e:
            reply = "Ups... Parker nggak bisa jawab sekarang. Coba cek koneksi atau API key kamu ya~"

        st.session_state.messages.append({"role": "assistant", "content": reply})
        st.rerun()
