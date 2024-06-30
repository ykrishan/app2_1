import streamlit as st
import pandas as pd
from Send_email import Send_mail



st.header("Contact Me")

topic_file = pd.read_csv('topics.csv')
with st.form(key='contact_form'):
    user_mail = st.text_input("Your Email Address")
    options = st.selectbox("What Topic do you want Discuss?", options=topic_file["topic"])
    raw_message = st.text_area("Your Message")
    message = f"""\
Subject: New emil from {user_mail}

From: {user_mail}
Topic: {options}
{raw_message}
"""
    submit = st.form_submit_button("Submit")

    if submit:
        Send_mail(message)
        st.info("Email sent successfully")
