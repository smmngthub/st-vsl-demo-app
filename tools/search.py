# Bismillahirrahumanirrahim
import streamlit as st
import pandas as pd

def load_data(data):
  pd.read_csv(data)

st.title("Adavance Search Section")

world = load_data("data_files/Vessels.csv")



