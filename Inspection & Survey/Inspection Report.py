#Bismillahirrahumanirrahim
import streamlit as st

st.title("You are in Inspection Report Page")

col1, col2 = st.columns(2)

with col1:
  with st.container(height=300):
    report_no = st.text_input("Report #", value="", placeholder="")
    marine = st.text_input("Marine")
    location = st.text_input("Location")
    inspector_name = st.text_input("Inspector Name")
    select_inspection_form = st.text_input("Select Inspection Form")

with col2:
  with st.container(height=300):
    vessel_number = st.text_input("Vessel Number")
    vessel_name = st.text_input("Vessel Name")
    registration_number = st.text_input("Registration Number")
    nautical_reading = st.text_input("Nautical Reading")

submit = st.button("Submit")
if (submit):
  st.success("You have successfully the information")
