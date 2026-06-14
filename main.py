import streamlit as st
import pandas as pd
import os
import folium
from streamlit_folium import st_folium

st.set_page_config(page_title="Vehicle Tracking Dashboard", layout="wide")

st.title("🚗 IoT Vehicle Tracking & Theft Prevention System")

file_path = "data/location_history.csv"

if os.path.exists(file_path):

    df = pd.read_csv(file_path)

    latest = df.iloc[-1]

    st.subheader("📍 Latest Vehicle Location")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Latitude", f"{latest['Latitude']:.6f}")

    with col2:
        st.metric("Longitude", f"{latest['Longitude']:.6f}")

    with col3:
        st.metric("Status", latest['Status'])

    st.subheader("🗺 Live Vehicle Location")

    m = folium.Map(
        location=[latest["Latitude"], latest["Longitude"]],
        zoom_start=15
    )

    folium.Marker(
        [latest["Latitude"], latest["Longitude"]],
        popup="Vehicle Location",
        tooltip="Vehicle"
    ).add_to(m)

    st_folium(m, width=700, height=500)

    st.subheader("📜 Recent Location History")
    st.dataframe(df.tail(10))

    st.subheader("🔗 Google Maps Link")
    st.write(latest["Google_Maps"])

else:
    st.warning("No location data found. Run vehicle_tracking.py first.")