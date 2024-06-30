import streamlit as st
from Send_email import Send_mail



st.header("Contact Me")

with st.form(key='contact_form'):
    user_mail = st.text_input("Your Email Address")
    raw_message = st.text_area("Your Message")
    message = f"""\
Subject: New emil from {user_mail}

From: {user_mail}
{raw_message}
"""
    submit = st.form_submit_button("Submit")

    if submit:
        Send_mail(message)
        st.info("Email sent successfully")
