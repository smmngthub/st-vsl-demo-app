# Bismillahirrahumanirrahim
import streamlit as st
from user_login import st_user_login 

st.write(" Bismillahirrahumanirrahim")
  
st.header("Testing...")
st.title("Bismillah")

st.write("Test" , __name__)
#if __name__ == '__main__':
app_user = st_user_login()
st.write(" Ret Value", app_user)


