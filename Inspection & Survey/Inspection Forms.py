# Bismillahirrahumanirrahim

import streamlit as st
st.title("You are in the Inspection Forms Page")


def collect_form_details():
  st.write("Add Inspection Item")

  inspect_item = st.text_input("Inspection Item")
  # rad_type = st.radio("Type", ("Good-Repair-Replace-NA", "Yes-No-NA", "Text Field", "Number", "Pass-Fail-NA", "Ok-Fault-NA")
  reqd = st.checkbox("Required")
  instruction = st.text_area("Instructions")
  

  save = st.button("Save")
  if save:
    st.success(" Successfully submitted the information")

collect_form_details()
