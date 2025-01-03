# Bismillahirrahumanirrahim
import streamlit as st

st.title(":green[Add Vessel]")


# New Vessels & List of Existing Vessels

New Vessel
New Vessel, Existing Vessels, Amendments = st.tabs(["New", "Existing", "Amendment"])\
with New Vessel:
  pass
with Existing Vessels:
  pass
with Amendments:
  pass

Vessel Number = st.text_input("Vessel Number")
Vessel Name = st.text_input("Vessel Name")
Vessel Category = st.text_input("Vessel Category")
Registration Number = st.text_input("Registration Number")
Model = st.text_input("Model")
Nautical Reading = st.text_input("Nautical Reading")
Nautical Miles = st.text_input("Nautical Miles")
Status = st.selectbox("Status", ("Available", "In Maintenance", "Maintenance Required"),) # DD 
Available = st.text_input("Available")
Flag = st.text_input("Flag") # DD  -Country
Port of Registry = st.text_input("Port of Registry")
Passanger Capacity = st.text_input("Passanger Capacity")
Chassis Number = st.text_input("Chassis Number")
Manufacture = st.text_input("Manufacture")
Last Departure Date  = st.text_input("Last Departure Date")
Last Service Reading  = st.text_input("Last Service Reading")
Last Service Date  = st.text_input("Last Service Date")
Registration Exp Date  = st.text_input("Registration Exp Date")
Site/Project  = st.text_input("Site/Project")
Business Unit  = st.text_input("Business Unit")
Vessel Value  = st.text_input("Vessel Value")
Purchase Date  = st.date_input("Purchase Date")
Warranty Date  = st.date_input("Warranty Date")
Required Geo Location while Inspection  = st.checkbox("Geo Location")
Assign Inspection Form  = st.text_input("Assign Inspection Form")


Operator Name  = st.text_input("Operator Name")
Maintenance Priority  = st.text_input("Maintenance Priority")
Normal  = st.text_input("Normal")
Ownership Mode  = st.text_input("Ownership Mode")
Vessel Note  = st.text_input("Vessel Note")
Vessel Image  = st.text_input("Vessel Image")
GPS EnabledDevice ID  = st.text_input("GPS EnabledDevice ID")
GPS Vessel ID  = st.text_input("GPS Vessel ID")

