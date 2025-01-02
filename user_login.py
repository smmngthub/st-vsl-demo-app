# Bismillahirrahumanirrahim
import streamlit as st

def st_user_login()

  try: 
    user_name = st.text_input(label="User Name", Value="Admin", placeholder="Please Enter Your Login", max_chars=20)

    st.snow()
  except:
    st.error("Error encountered in logging in")
  
