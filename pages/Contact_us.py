import streamlit as st
from files import send_email
st.header("Hello, you can contact me")

with st.form(key="send_email"):
    email_value = st.text_input("Your email address")
    message_value = st.text_area("Your massage")
    message = f"""
    Subject: New message from {email_value}
    From: {email_value}
    {message_value}
    """
    submit_btn = st.form_submit_button("Submit")
    if submit_btn:
        send_email.send_email(message)
        st.info("Sizning xabaringiz sended chotki")
