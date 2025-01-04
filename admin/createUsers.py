# Bismillahirrahumanirrahim
import streamlit as st

st.title(":orange[User Creation]")
def create_new_users():

  # with st.form(key="user_creation")
  
  user_name = st.text_input("User Name")
  st.write("User Name", user_name)
  pwd = st.text_input("You Password", type=password, placeholder="Please enter your password")
  re-pwd = st.text_input("Re-Enter Password", type=password, placeholder="Please re-enter your password")
  btn_register = st.button("Register")
  
  return True

user_action = st.radio("Action", ["New User", "Existing"], horizontal=True)
if user_action == "New User":
  # call the form to enter the New Users
  create_new_users()
  pass
elif user_action == "Existing":
  pass

def toggle_and_text()
  cols = st.columns(2)
  cols[0].toggle("Toggle") 
  cols[1].text_area("Enter Text")
  
toggle_and_text()
