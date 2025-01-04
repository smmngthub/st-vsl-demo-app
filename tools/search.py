# Bismillahirrahumanirrahim
import streamlit as st
import pandas as pd

def load_data(data):
  return pd.read_csv(data)

st.title("Adavance Search Section")

vessels = load_data("data_files/Vessels.csv")
world = load_data("data_files/worldcities.csv")

with st.expander("Vessels View"):
  st.dataframe(vessels, hide_index=True)

with st.expander("Cities View"):
  st.dataframe(world, hide_index=True)

cities_list = world["city"].unique().tolist()

selected_city = st.multiselect("Cities", cities_list, default=["Chennai"])

with st.expander("Filtered View"):
  df = world[world["city"].isin(selected_city)]
  st.dataframe(df)


