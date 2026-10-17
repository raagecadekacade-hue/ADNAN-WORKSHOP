import streamlit as st

left, center, right = st.columns([1, 3, 1])
with center:
    st.title("ADNAnS WORKSHOP")
with st.form("registration"):
    name = st.text_input("name")
    email = st.text_input("email")
    track = st.selectbox("Track", ["python", "React", "AI"])
    submitted = st.form_submit_button("Registred", type="primary")

    if submitted:
        st.success(f"Welcome abord {name}")
