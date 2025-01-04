# Bismillahirrahumanirrahim

import streamlit as st
#st.title("You are in the Inspection Forms Page")
title_writing = "Inspection Form"
title_format = f'<p style="text-align: center; font-family: ' \
               f'Arial; color: #808080; font-size: 40px; ' \
               f'font-weight: bold;">{title_writing}</p>'
st.markdown(title_format, unsafe_allow_html=True)

# st.subheader("_Streamlit_ is :blue[cool] :sunglasses:")
# st.subheader("This is a subheader with a divider", divider="gray")
# st.subheader("These subheaders have rotating dividers", divider=True)

st.subheader("Add :blue[Inspection] Item :sunglasses:", divider=True)

def collect_form_details():
  # st.write("Add Inspection Item")
  # st.write("---")
  inspect_item = st.text_input("Inspection Item")
  rad_type = st.radio("Type", ["Good-Repair-Replace-NA", "Yes-No-NA", "Text Field", "Number", "Pass-Fail-NA", "Ok-Fault-NA"], horizontal=True)
  reqd = st.checkbox("Required")
  instruction = st.text_area("Instructions")
  

  save = st.button("Save")
  if save:
    st.success(" Successfully submitted the information")
    st.snow()

collect_form_details()
