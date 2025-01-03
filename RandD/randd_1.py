# Bismillahirrahumanirrahim

import streamlit as st
import datetime # to capture the DOB
import sqlite3  # to store the information in the local database
# conn=
# https://fonts.google.com/icons?icon.size=24&icon.color=%23e8eaed - Reference for Icons
st.title("You are in RANDD_1.py page")
st.snow()
st.toast("Welcome to the R & D World")

# Create a Form
def test_form():
  st.subtitle(" This is a TEST Form for SQLite3")
  with st.form(key="Test Info Form"):
    # Collect the basic information
    name = st.text_input(label="First Name:" )
    age = st.number_input("You Age", value=None, placeholder="Type a number...")
    dob = st.date_input("When's your birthday", value=None)

    btn_submit = st.form_submit_button(label="Submit")
    if btn_submit:
      st.success("You have successfully submitted the details. Thank you!")
      st.balloons()
      
test_form()


