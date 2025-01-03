# Bismillahirrahumanirrahim
import streamlit as st

st.title(":Orange[User Creation]")
def create_new_users():

  # with st.form(key="user_creation")
  user_name = st.text_input("Useer Name")
  st.write("USer Name", user_name)
    
  
  return True

user_action = st.radio("Action", ["New User", "Existing"], horizontal=True)
if user_action == "New User":
  # call the form to enter the New Users
  create_new_users()
  pass
elif user_action == "Existing":
  pass
