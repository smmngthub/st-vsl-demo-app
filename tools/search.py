# Bismillahirrahumanirrahim
import streamlit as st
import pandas as pd

def load_data(data):
  return pd.read_csv(data)

st.title("Adavance Search Section")

vessels = load_data("data_files/Vessels.csv")

with st.expander("Vessels View"):
  st.dataframe(vessels)

