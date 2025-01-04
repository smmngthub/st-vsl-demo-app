# Bismillahirrahumanirrahim
import streamlit as st
import time
import datetime
import sqlite3

st.title(":green[Add Vessel]")

# New Vessels & List of Existing Vessels

# DATABASE STARTS HERE

def add_vessel_data(a, b, c, d, e, f, g, h):
  st.toast("CREAT ing TABLE...")
  time.sleep(.5)
  conn = sqlite3.connect('vesseldb.db')
  cur = conn.cursor()
  cur.execute("""CREATE TABLE IF NOT EXISTS vessel_table(
    Vessel_Number TEXT(50), Vessel_Name TEXT(50), Vessel_Category TEXT(50), Registration_Number TEXT(50), 
    Model TEXT(50), Status TEXT(50), Flag TEXT(50), Port_of_Registry TEXT(50)
    );""")
  st.toast("INSERT ing to TABLE...")
  time.sleep(.5)

  cur.execute("INSERT INTO vessel_table VALUES (?, ?, ?, ?, ?, ?, ?, ?)", (a, b, c, d, e, f, g, h))
  # st.info("Inside add_test_data - Before COMMIT")
  st.toast("Performing COMMIT...", icon='😍')
  time.sleep(.5)

  conn.commit()
  conn.close() # Not Closing it here are we need the connection later to retrieve the data
  st.success("You have successfully submitted the details. Thank you!")
  st.balloons()  
# Calling the form 
def fetch_vessel_data():
  st.toast("Fetching data...")
  time.sleep(.5)
  try:
    conn = sqlite3.connect('vesseldb.db')
    cur = conn.cursor()
    cur.execute("SELECT * from vessel_table")
    all_info = cur.fetchall()
    conn.commit()
    conn.close()
    st.toast("Fetching ALL data!", icon='🎉') 
    return all_info
  except Exception as e:
    st.error(f" There is a major problem with the retrival of data ::>>{e}")
  # return None
  # st.info("Inside fetcg_tst_data - Before CLOSE")

def delete_vessel_data():
  try:
    st.toast("Inside DELETE ALL")
    time.sleep(1)
    conn = sqlite3.connect('vesseldb.db')
    cur = conn.cursor()
    cur.execute("DELETE from vessel_table")
    st.toast("After DELETE ALL")
    time.sleep(1)
    
    # all_info = cur.fetchall()
    conn.commit()
    conn.close()
    st.toast("DELET ing ALL data!", icon='🎉') 
    # pass
  except Exception as e:
    st.error(f" There is a major problem with the deletion of data ::>>{e}")
  # pass


#  ENDS HERE

def add_new_vessel():

  col_left, col_right = st.columns([1, 1])

  with col_left:
    with st.container(height=600):
      Vessel_Number = st.text_input(":red[*Vessel Number]")
      Vessel_Name = st.text_input(":red[*Vessel Name]")
      Vessel_Category = st.text_input(":red[*Vessel Category]")
      Registration_Number = st.text_input(":red[*Registration Number]")
      Model = st.text_input("Model")
      Nautical_Reading = st.text_input("Nautical Reading")
      Nautical_Miles = st.text_input("Nautical Miles")

    with st.container(height=300):
      Status = st.selectbox("*Status", ("Available", "In Maintenance", "Maintenance Required")) # DD 
      Flag = st.text_input("Flag") # DD  -Country
      Port_of_Registry = st.text_input("Port of Registry")  

    with st.container(height=300):
      SiteProject  = st.text_input("Site/Project")
      Business_Unit  = st.text_input("Business Unit")
      Vessel_Value  = st.text_input("Vessel Value")

    with st.container(height=400):
      Purchase_Date  = st.date_input("Purchase Date")
      Warranty_Date  = st.date_input("Warranty Date")
      Required_Geo_Location_while_Inspection  = st.checkbox("Geo Location")
  
      Assign_Inspection_Form  = st.text_input("Assign Inspection Form")

    # pass
  with col_right:
    with st.container(height=600):
      Passanger_Capacity = st.text_input("Passanger Capacity")
      Chassis_Number = st.text_input("Chassis Number")
      Manufacture = st.text_input("Manufacture")
      Last_Departure_Date  = st.date_input("Last Departure Date")
      Last_Service_Reading  = st.text_input("Last Service Reading")
      Last_Service_Date  = st.date_input("Last Service Date")
      Registration_Exp_Date  = st.date_input("Registration Exp Date")

    with st.container(height=350):
      Operator_Name  = st.text_input("Operator Name")
      Maintenance_Priority  = st.text_input("Maintenance Priority")
      Normal  = st.text_input("Normal")
      Ownership_Mode  = st.text_input("Ownership Mode")
      Vessel_Note  = st.text_input("Vessel Note")

    with st.container(height=100):
      Vessel_Image  = st.text_input("Vessel Image") # Upload Image 

    with st.container(height=150):
      GPS_EnabledDevice_ID  = st.text_input("GPS EnabledDevice ID")
      GPS_Vessel_ID  = st.text_input("GPS Vessel ID")
  
  #pass
      

  if st.button("Add Vessel"):
    add_vessel_data(Vessel_Number, Vessel_Name, Vessel_Category, Registration_Number, Model, Status, Flag, Port_of_Registry)
    st.success(f"You have successfully added the new vessel {Vessel_Name}")
    st.balloons()
    time.sleep(1)
  
  return None

def list_existing_vessel():
  all_vessels = fetch_vessel_data()
  st.dataframe(all_vessels)
  # st.write("Amendments")
  #pass
  
user_action = st.radio("Action", ["New Vessel", "Existing", "Amendment", "TAB Format"], horizontal=True)
# st.write("User Action is ", user_action) 
st.divider()
if st.button("Delete All"):
  # call javascript popup to get confirmation from the user. If yes, proceed
  delete_vessel_data()
  # st.toast("Sorry to see the Vessel LEAVVING...")
  pass 
  
if user_action == "New Vessel":
  # st.write("New Vessel ", user_action)
  add_new_vessel()
elif user_action == "Existing":
  # st.write("Existing ", user_action)
  list_existing_vessel()
elif user_action == "Amendment":
  # st.write("Amendment Vessel ", user_action)
  pass
elif user_action == "TAB Format":
  # st.write("TAB ", user_action)
  pass
  
  NewVessel, ExistingVessels, Amendments = st.tabs(["New", "Existing", "Amendment"])
  with NewVessel:
    add_new_vessel()
    pass
  with ExistingVessels:
    pass
  with Amendments:
    pass
  
