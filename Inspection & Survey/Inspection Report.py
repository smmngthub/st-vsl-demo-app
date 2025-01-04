#Bismillahirrahumanirrahim
import streamlit as st

st.title("You are in Inspection Report Page")
# This is a 3 step process
# 1. Inspection Info
# 2. Do Inspection
# 3. Inspection Summary

def do_inspection():
  # screen field
  
  pass

def inspection_summary():
  # screen fields

  with st.container(key="ins_summary", border=True):  
  # Overall Condition : DD List (Excellant Condition, Good Condition, A little wear, 
    safe_to_use = st.radio("Vessel Safe to Use", ["Yes", "No"]) 
    maint_reqd = st.radio("Maintenance Required:", ["Yes", "No"])
    vsl_status = st.selectbox("Vessel Status :",  ("Available", "In Maintenance", "Maintenance Required", "Breakdown", "Discontinue")) 
    maint_priority = st.selectbox("Maintenance Priority :", ("Low", "Medium", "High", "Emergency"))
    additional_note = st.text_area("Additional Note")
  

col1, col2 = st.columns(2)

with col1:
  with st.container(height=350):
    report_no = st.text_input("Report #", value="", placeholder="")
    marine = st.text_input("Marine")
    location = st.text_input("Location")
    inspector_name = st.text_input("Inspector Name")
    select_inspection_form = st.text_input("Select Inspection Form")

with col2:
  with st.container(height=350):
    vessel_number = st.text_input("Vessel Number")
    vessel_name = st.text_input("Vessel Name")
    registration_number = st.text_input("Registration Number")
    nautical_reading = st.text_input("Nautical Reading")

next = st.button("Next")
if (next):
  
  inspection_summary()

  submit = st.button("Submit")
  if submit:
    st.success("You have successfully the information")
    st.balloons()
  
# 1. Inspection Info
# 2. Do Inspection
# 3. Inspection Summary

