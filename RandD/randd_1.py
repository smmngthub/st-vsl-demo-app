# Bismillahirrahumanirrahim
# https://fonts.google.com/icons?icon.size=24&icon.color=%23e8eaed - Reference for Icons
import streamlit as st
import pandas as pd 
import datetime # to capture the DOB
import time
# from st_aggrid import AgGrid
# from streamlit_push_notifications import send_alert

import sqlite3  # to store the information in the local database
# conn = sqlite3.connect('testdb.db', check_same_thread=False)
# cur = conn.cursor()
# st.write(" Connection :", conn) 
# st.write(" Cur: " , cur)
# st.title("You are in RANDD_1.py page")
# st.title (":balloon:")
st.snow()
# st.toast("Welcome to the R & D World")

# Create a Form
def test_form():
  st.subheader(" This is a TEST Form for SQLite3")
  with st.form(key="Test Info Form"):
    # Collect the basic information
    name = st.text_input(label="First Name:", value="" )
    age = st.number_input("You Age", value=25, step=1, placeholder="Type a number...")
    dob = st.date_input("When's your birthday", value=None)

    btn_submit = st.form_submit_button(label="Submit")
    if btn_submit:
      # Validate the Input
      if age <18 or age > 120:
        st.error(f" You entered the age as {age}. Please enter a number between 18 and 120.")
        st.stop()
      else:  
        st.toast("Information is being SUBMITTED...")
        time.sleep(.5)
        # st.info("You are inside SUBIT Button")
        add_test_data(name, age, dob)  

def add_test_data(a, b, c):
  st.toast("CREAT ing TABLE...")
  time.sleep(.5)
  conn = sqlite3.connect('testdb.db')
  cur = conn.cursor()
  cur.execute("""CREATE TABLE IF NOT EXISTS tst_table(NAME TEXT(50), AGE TEXT(50), DOB TEXT(20));""")
  st.toast("INSERT ing to TABLE...")
  time.sleep(.5)

  cur.execute("INSERT INTO tst_table VALUES (?, ?, ?)", (a, b, c))
  # st.info("Inside add_test_data - Before COMMIT")
  st.toast("Performing COMMIT...", icon='😍')
  time.sleep(.5)

  conn.commit()
  conn.close() # Not Closing it here are we need the connection later to retrieve the data
  st.success("You have successfully submitted the details. Thank you!")
  st.balloons()  
# Calling the form 
def fetch_tst_data():
  st.toast("Fetching data...")
  time.sleep(.5)
  try:
    conn = sqlite3.connect('testdb.db')
    cur = conn.cursor()
    cur.execute("SELECT * from tst_table")
    all_info = cur.fetchall()
    conn.commit()
    conn.close()
    st.toast("Fetching ALL data!", icon='🎉') 
    return all_info
  except Exception as e:
    st.error(f" There is a major problem with the retrival of data ::>>{e}")
  # return None
  # st.info("Inside fetcg_tst_data - Before CLOSE")

def delete_tst_data():
  try:
    st.toast("Inside DELETE ALL")
    time.sleep(1)
    conn = sqlite3.connect('testdb.db')
    cur = conn.cursor()
    cur.execute("DELETE from tst_table")
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

# df = fetch_tst_data()

form_col, list_col = st.columns([4,1])
with form_col:
  #st.write(" All Info", df) 
  if st.button("Delete All"):
    delete_tst_data()
    # pass
with list_col:
  # st.dataframe(df)
  if st.button("Alert Me!"):
    pass
    #send_alert("This is an ALERT Message")  # This is not working as the from ... import send_alert is NOT working
  #pass

def dataframe_selected(df):
  df_copy = df.copy()
  df_copy.insert(0, 'Action', True)

  edited_df = st.data_editor(
    df_copy, hide_index=True, 
    column_config={
      "Action": st.column_config.CheckboxColumn(required=True)
    },
    #disabled=df.columns,
  )
  
  selected_rows = edited_df[edited_df.Action]
  
  return selected_rows.drop(['Action'], axis=1)

tab1, tab2, tab3, tab4, tab5 = st.tabs(["Add Entry", "🗃 View Info (Table)", "View Info (Tree)", "Delete Info", "AgGrid"])

with tab1:
  test_form()
  # st.rerun()
  # pass
with tab2:
  # if len(df) > 0:
  df = fetch_tst_data()
  st.dataframe(df)
  #pass
with tab3:
  #if len(df) > 0:
  df = fetch_tst_data()
  st.write(" All Info", df)
with tab4:
  #if len(df) > 0:
  df = pd.DataFrame(fetch_tst_data())
  st.dataframe(df)
with tab5:
  df = pd.DataFrame(fetch_tst_data())
  selected = dataframe_selected(df)
  st.dataframe(selected)
  

  

