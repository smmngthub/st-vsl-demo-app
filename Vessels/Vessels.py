# Bismillahirrahumanirrahim
import streamlit as st
import time
import datetime

st.title(":green[Add Vessel]")

# New Vessels & List of Existing Vessels


def add_new_vessel():

  col_left, col_right = st.columns([1, 1])

  with col_left:
    Vessel_Number = st.text_input(":red[*Vessel Number]")
    Vessel_Name = st.text_input(":red[*Vessel Name]")
    Vessel_Category = st.text_input(":red[*Vessel Category]")
    Registration_Number = st.text_input(":red[*Registration Number]")
    Model = st.text_input("Model")
    Nautical_Reading = st.text_input("Nautical Reading")
    Nautical_Miles = st.text_input("Nautical Miles")
    Status = st.selectbox("*Status", ("Available", "In Maintenance", "Maintenance Required")) # DD 
    Flag = st.text_input("Flag") # DD  -Country
    Port_of_Registry = st.text_input("Port of Registry")  

    SiteProject  = st.text_input("Site/Project")
    Business_Unit  = st.text_input("Business Unit")
    Vessel_Value  = st.text_input("Vessel Value")
    
    Purchase_Date  = st.date_input("Purchase Date")
    Warranty_Date  = st.date_input("Warranty Date")
    Required_Geo_Location_while_Inspection  = st.checkbox("Geo Location")

    Assign_Inspection_Form  = st.text_input("Assign Inspection Form")

    # pass
  with col_right:
    Passanger_Capacity = st.text_input("Passanger Capacity")
    Chassis_Number = st.text_input("Chassis Number")
    Manufacture = st.text_input("Manufacture")
    Last_Departure_Date  = st.date_input("Last Departure Date")
    Last_Service_Reading  = st.text_input("Last Service Reading")
    Last_Service_Date  = st.date_input("Last Service Date")
    Registration_Exp_Date  = st.date_input("Registration Exp Date")

    Operator_Name  = st.text_input("Operator Name")
    Maintenance_Priority  = st.text_input("Maintenance Priority")
    Normal  = st.text_input("Normal")
    Ownership_Mode  = st.text_input("Ownership Mode")
    Vessel_Note  = st.text_input("Vessel Note")
    Vessel_Image  = st.text_input("Vessel Image") # Upload Image 
    GPS_EnabledDevice_ID  = st.text_input("GPS EnabledDevice ID")
    GPS_Vessel_ID  = st.text_input("GPS Vessel ID")
  
  #pass
      

  if st.button("Add Vessel"):
    st.success(f"You have successfully added the new vessel {Vessel_Name}")
    st.balloons()
    time.sleep(1)
  
  return None

def list_existing_vessel():
  st.write("Amendments")
  pass
  
user_action = st.radio("Action", ["New Vessel", "Existing", "Amendment", "TAB Format"], horizontal=True)
# st.write("User Action is ", user_action) 
st.divider()

if user_action == "New Vessel":
  # st.write("New Vessel ", user_action)
  add_new_vessel()
elif user_action == "Existing":
  # st.write("Existing ", user_action)
  list_existing_vessel()
elif user_action == "Amendment":
  # st.write("Amendment Vessel ", user_action)
elif user_action == "TAB Format":
  # st.write("TAB ", user_action)
  
  NewVessel, ExistingVessels, Amendments = st.tabs(["New", "Existing", "Amendment"])
  with NewVessel:
    add_new_vessel()
    pass
  with ExistingVessels:
    pass
  with Amendments:
    pass
  
