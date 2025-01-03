# Bismillahirrahumanirrahim
# https://fonts.google.com/icons?icon.size=24&icon.color=%23e8eaed - Reference for Icons
import streamlit as st
import pandas as pd 
import datetime # to capture the DOB
import time
from streamlit_push_notifications import send_alert

import sqlite3  # to store the information in the local database
conn = sqlite3.connect('testdb.db', check_same_thread=False)
cur = conn.cursor()

st.title("You are in RANDD_1.py page")
# st.title (":balloon:")
st.snow()
st.toast("Welcome to the R & D World")

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
      st.toast("Information is being SUBMITTED...")
      time.sleep(.5)
      # st.info("You are inside SUBIT Button")
      add_test_data(name, age, dob)  

def add_test_data(a, b, c):
  st.toast("CREAT ing TABLE...")
  time.sleep(.5)
  cur.execute("""CREATE TABLE IF NOT EXISTS tst_table(NAME TEXT(50), AGE TEXT(50), DOB TEXT(20));""")
  st.toast("INSERT ing to TABLE...")
  time.sleep(.5)

  cur.execute("INSERT INTO tst_table VALUES (?, ?, ?)", (a, b, c))
  # st.info("Inside add_test_data - Before COMMIT")
  st.toast("Performing COMMIT...", icon='😍')
  time.sleep(.5)

  conn.commit()
  #conn.close() # Not Closing it here are we need the connection later to retrieve the data
  #st.success("You have successfully submitted the details. Thank you!")
  st.balloons()  
# Calling the form 
def fetch_tst_data():
  st.toast("Fetching data...")
  time.sleep(.5)
  cur.execute("SELECT * from tst_table")
  all_info = cur.fetchall()

  conn.commit()
  st.toast("Fetching ALL data!", icon='🎉') 
  return all_info
  # st.info("Inside fetcg_tst_data - Before CLOSE")


form_col, list_col = st.columns([4,1])
df = fetch_tst_data()
with form_col:
  # st.write(" All Info", df) 
  pass
with list_col:
  # st.dataframe(df)
  if st.button("Alert Me!"):
    send_alert("This is an ALERT Message")  
  #pass
tab1, tab2, tab3 = st.tabs(["Entry", "🗃 Listing", "Selection"])

with tab1:
  test_form()
  pass
with tab2:
  st.write(" All Info", df) 
with tab3:
  st.dataframe(df)

