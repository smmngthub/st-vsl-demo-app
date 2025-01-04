#Bismillahirrahumanirrahim
import streamlit as st

# st.title("You are in Inspection Report Page")
title_writing = "Inspection Report"
title_format = f'<p style="text-align: center; font-family: ' \
               f'Arial; color: #808080; font-size: 40px; ' \
               f'font-weight: bold;">{title_writing}</p>'
st.markdown(title_format, unsafe_allow_html=True)

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
    col1, col2 = st.columns(2)
    with col1: 
      safe_to_use = st.radio("Vessel Safe to Use", ["Yes", "No"], horizontal=True) 
      maint_reqd = st.radio("Maintenance Required:", ["Yes", "No"], horizontal=True)
    with col2:
      vsl_status = st.selectbox("Vessel Status :",  ("Available", "In Maintenance", "Maintenance Required", "Breakdown", "Discontinue")) 
      maint_priority = st.selectbox("Maintenance Priority :", ("Low", "Medium", "High", "Emergency"))
    additional_note = st.text_area("Additional Note")
  
def inspection_info():
  st.write("Inspection Information")
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
  
  stg1 = st.button("Next")
  if (stg1):

    
    inspection_summary()
    
    submit = st.button("Submit")
    if submit:
      st.success("You have successfully the information")
      st.balloons()
  
# 1. Inspection Info
inspection_info()
# 2. Do Inspection
# 3. Inspection Summary

