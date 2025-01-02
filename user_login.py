# Bismillahirrahumanirrahim
import streamlit as st

def st_user_login():

  try: 
    user_name = st.text_input(label="User Name", value="Admin", placeholder="Please Enter Your Login", max_chars=20)
    user_pwd = st.text_input(label="Password", placeholder="Please enter your passwod", max_chars=25)

    submitted = st.button("Login")
    
    # trimmed_user_name = user_name.trim()
    # trimmed_user_pwd = user_pwd.trim() 
    # if len(user_name) > 1 and user_name = "Vessel123" and user_pwd = "Hey@123"
    if submitted 
      if user_name == "Vessel123" and user_pwd == "Hey@123":  
        st.snow()
        st.success("You have successfully logged in to the system")
      elif:
        st.error("Error, entering user name and/or password. Please contact the Administrator")
    return submitted
  except:
    st.error(f"Error encountered in logging in {e}")
    st.stop()
