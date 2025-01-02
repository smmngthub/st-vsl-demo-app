# Bismillahirrahumanirrahim
import streamlit as st
from user_login import st_user_login 

st.subheader("Bismillahirrahumanirrahim")

app_user = st_user_login()
if app_user == "VSL":
  st.toast("Hi you are in Vessel Application")
  # Build the sidebar
  with st.sidebar:
    st.subheader = "Vessels"
    st.divider()
  # Build the Main Navigations  
elif app_user == "TBT":
  
  st.toast("Hi you are in TBT Application")
  st.balloons()
  
  # Build the sidebar
  with st.sidebar:
    pass
    
  # Build the Main Navigations
else:
  st.toast("Somehting wrong Happened")
  st.error("Somehting wrong Happened")

  
