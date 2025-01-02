# Bismillahirrahumanirrahim
import streamlit as st
from user_login import st_user_login 

st.subheader("Bismillahirrahumanirrahim")

app_user = st_user_login()
if app_user == "VSL":
  st.toast("Hi you are in Vessel Application")
  # Build the sidebar
  
  # Build the Main Navigations  
elif app_user == "TBT":
  st.toast("Hi you are in TBT Application")
  # Build the sidebar
  # Build the Main Navigations
elif:
  st.toast("Somehting wrong Happened")
  st.error("Somehting wrong Happened")

  
