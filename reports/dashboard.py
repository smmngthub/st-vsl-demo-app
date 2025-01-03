# Bismillahirrahumanirrahim

import streamlit as st
import numpy as np
# import matplotlib.pyplot as plt

st.title("Dash Board")
title_writing = "Dash Board"
title_format = f'<p style="text-align: center; font-family: ' \
               f'Arial; color: #808080; font-size: 40px; ' \
               f'font-weight: bold;">{title_writing}</p>'
st.markdown(title_format, unsafe_allow_html=True)

a, b = st.columns(2)
c, d = st.columns(2)

a.metric("Temperature", "30°F", "-9°F", border=True)
b.metric("Wind", "4 mph", "2 mph", border=True)

c.metric("Humidity", "77%", "5%", border=True)
d.metric("Pressure", "30.34 inHg", "-2 inHg", border=True)

st.title("Interactive Data Visualization")

# Slider for selecting a number
number = st.slider("Select a number", 1, 100)

# Generate random data
data = np.random.randn(number)

# Create a histogram
# plt.hist(data, bins=20)
# st.pyplot(plt)

