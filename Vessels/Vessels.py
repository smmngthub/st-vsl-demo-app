# Bismillahirrahumanirrahim
import streamlit as st
import time
import datetime

st.title(":green[Add Vessel]")

# New Vessels & List of Existing Vessels


def add_new_vessel():
  Vessel_Number = st.text_input("Vessel Number")
  Vessel_Name = st.text_input("Vessel Name")
  Vessel_Category = st.text_input("Vessel Category")
  Registration_Number = st.text_input("Registration Number")
  Model = st.text_input("Model")
  Nautical_Reading = st.text_input("Nautical Reading")
  Nautical_Miles = st.text_input("Nautical Miles")
  Status = st.selectbox("Status", ("Available", "In Maintenance", "Maintenance Required"),) # DD 
  Available = st.text_input("Available")
  Flag = st.text_input("Flag") # DD  -Country
  Port_of_Registry = st.text_input("Port of Registry")
  Passanger_Capacity = st.text_input("Passanger Capacity")
  Chassis_Number = st.text_input("Chassis Number")
  Manufacture = st.text_input("Manufacture")
  Last_Departure_Date  = st.text_input("Last Departure Date")
  Last_Service_Reading  = st.text_input("Last Service Reading")
  Last_Service_Date  = st.text_input("Last Service Date")
  Registration_Exp_Date  = st.text_input("Registration Exp Date")
  SiteProject  = st.text_input("Site/Project")
  Business_Unit  = st.text_input("Business Unit")
  Vessel_Value  = st.text_input("Vessel Value")
  Purchase_Date  = st.date_input("Purchase Date")
  Warranty_Date  = st.date_input("Warranty Date")
  Required_Geo_Location_while_Inspection  = st.checkbox("Geo Location")
  Assign_Inspection_Form  = st.text_input("Assign Inspection Form")
  
  
  Operator_Name  = st.text_input("Operator Name")
  Maintenance_Priority  = st.text_input("Maintenance Priority")
  Normal  = st.text_input("Normal")
  Ownership_Mode  = st.text_input("Ownership Mode")
  Vessel_Note  = st.text_input("Vessel Note")
  Vessel_Image  = st.text_input("Vessel Image")
  GPS_EnabledDevice_ID  = st.text_input("GPS EnabledDevice ID")
  GPS_Vessel_ID  = st.text_input("GPS Vessel ID")
  
  if st.submit("Add Vessel"):
    st.success("You have successfully added the new vessel {Vessel_Name}")
    st.balloons()
    time.sleep(1)
  
  return true

NewVessel, ExistingVessels, Amendments = st.tabs(["New", "Existing", "Amendment"])
with NewVessel:
  add_new_vessel()
  pass
with ExistingVessels:
  pass
with Amendments:
  pass
  
