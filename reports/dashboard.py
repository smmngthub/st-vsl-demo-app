# Bismillahirrahumanirrahim

import streamlit as st
import numpy as np
# import matplotlib.pyplot as plt

# st.title("Dash Board")
title_writing = "Dash Board"
title_format = f'<p style="text-align: center; font-family: ' \
               f'Arial; color: #808080; font-size: 40px; ' \
               f'font-weight: bold;">{title_writing}</p>'
st.markdown(title_format, unsafe_allow_html=True)

st.bar_chart({"data": [1, 5, 2, 6, 2, 1]})

with st.expander("See explanation"):
    st.write('''
        The chart above shows some numbers I picked for you.
        I rolled actual dice for these, so they're *guaranteed* to
        be random.
    ''')
    st.image("https://static.streamlit.io/examples/dice.jpg")


st.title("Interactive Data Visualization")

# Slider for selecting a number
number = st.slider("Select a number", 1, 100)

# Generate random data
data = np.random.randn(number)

# Create a histogram
# plt.hist(data, bins=20)
# st.pyplot(plt)

