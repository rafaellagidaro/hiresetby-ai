import streamlit as st
import requests

st.title("🚀 Hiresetby AI")

# LOGIN
user = st.text_input("Usuário")
pwd = st.text_input("Senha", type="password")

if user == "admin" and pwd == "123":

    st.success("Login OK")

    tempo = st.slider("Tempo de resposta", 0, 10)
    feedback = st.selectbox("Feedback", [0, 1])
    score = st.slider("Score currículo", 0, 100)

    if st.button("Prever"):

        res = requests.post(
            "https://SUA_API.onrender.com/predict",
            json={
                "tempo_resposta": tempo,
                "feedback_bin": feedback,
                "score_curriculo": score
            }
        )

        st.write(res.json())

else:
    st.warning("Faça login")
