import folium
import streamlit as st
import pandas as pd
from streamlit_folium import st_folium


data = pd.read_csv("earthquakes_real.csv")


st.set_page_config(layout="wide")

st.title("Global Earthquake Map")

mean_lat = data["Latitude"].mean()
mean_lon = data["Longitude"].mean()


m = folium.Map(location=[mean_lat, mean_lon], zoom_start=2)

for i, row in data.iterrows():
    loc = row['Location']
    mag = row['Magnitude']
    folium.CircleMarker(
        location=[row["Latitude"], row["Longitude"]],
        radius=row["Magnitude"] * 2,
        popup=f"{row['Location']}: Magnitude {row['Magnitude']}",
        tooltip=f"Loc: {loc} Mag: {mag}",
        color='crimson',
        fill=True,
        fill_color='crimson'
    ).add_to(m)

st_folium(m, width=1400)