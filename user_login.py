# Bismillahirrahumanirrahim
import streamlit as st

def st_user_login():

  try: 
    user_name = st.text_input(label="User Name", value="Admin", placeholder="Please Enter Your Login", max_chars=20)

    st.snow()
  except:
    st.error(f"Error encountered in logging in {e}")
  
