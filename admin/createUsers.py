# Bismillahirrahumanirrahim
import streamlit as st

st.title(":green[User Creation]")

def create_new_users():
  # with st.form(key="user_creation")
  
  user_name = st.text_input("User Name 👇", max_chars=30, placeholder="Please enter a user name", help="User name cannot exceed 30")
  pwd = st.text_input("Your Password 👇", type="password", placeholder="Please enter a password", help="Password must contain special characters #@$")
  re_pwd = st.text_input("Re-Enter Password 👉", type="password", placeholder="Please re-enter your password", help="Password must contain special characters #@$")
  
  btn_register = st.button("Register")
  if btn_register:
    st.success("You have successfully submitted your information")
    st.balloons()
    st.snow()
  
  return True

user_action = st.radio("Action", ["New User", "Existing"], horizontal=True)
if user_action == "New User":
  # call the form to enter the New Users
  create_new_users()
  on = st.toggle("Take Picture")
  if on:
    pic_type = st.radio("Pic Mode", ["Upload", "Camera"], horizontal=True)
    # st.write("Picture Type: ", pic_type)
    if pic_type == "Upload":
      uploaded_photo = st.file_uploader("Upload a Photo", type=["png", "jpeg", "jpg"])
      pass
    elif pic_type == "Camera":
      camera_photo = st.camera_input("Take a Photo")
      if camera_photo is not None:
        st.write(" Hi Camera Photo")
      pass
    # toggle_and_pic()
  
  # pass
elif user_action == "Existing":
  pass


def toggle_and_text():
  cols = st.columns(2)
  cols[0].toggle("Toggle") 
  cols[1].text_area("Enter Text")
  # pass
  
