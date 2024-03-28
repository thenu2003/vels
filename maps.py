import streamlit as st
import requests
import folium

import plotly.express as px

import pandas as pd
with st.sidebar:
    sel = st.radio(
        "Navigation",
        ["Maps","Dashboard"],
        index=0
    )


if sel == 'Maps':
# Function to fetch live coordinates from HERE Maps Geocoding API
        def fetch_coordinates(location):
            api_key = "i0_zjfdg5wfXx-wwpLxzbwq4ngVYKMEVI4gq132atoY"
            base_url = "https://geocode.search.hereapi.com/v1/geocode"

            params = {
                "q": location,
                "apiKey": api_key
            }

            response = requests.get(base_url, params=params)
            data = response.json()

            if "items" in data and data["items"]:
                latitude = data["items"][0]["position"]["lat"]
                longitude = data["items"][0]["position"]["lng"]
                return latitude, longitude
            else:
                return None, None

        # Streamlit app
        def main():
            st.title('Live Location Map')
            st.write("This is a simple map showing your live location.")
            
            live_comapany= st.sidebar.text_input("Enter company name ")
                
            live_stock= st.sidebar.number_input("Enter your stock quantity:", value=0)

            # Get live location coordinates from HERE Maps Geocoding API
            location = "Madurai"  # Example location
            live_latitude, live_longitude = fetch_coordinates(location)

            if live_latitude is not None and live_longitude is not None:
                
                # Create a Folium map centered around the live location
                folium_map = folium.Map(location=[live_latitude, live_longitude], zoom_start=12)
                folium.Marker([live_latitude, live_longitude], popup=location).add_to(folium_map)

                # Get the HTML representation of the Folium map
                folium_html = folium_map._repr_html_()

                # Display the HTML representation using Streamlit
                st.components.v1.html(folium_html, width=700, height=500)
            else:
                st.error("Unable to fetch coordinates.")

        if __name__ == "__main__":
            main()
if sel == 'Dashboard':
        def load_data():
            data = pd.read_csv('CO2 Emissions_Canada.csv')
            return data
        data = load_data()

        # Dashboard title
        st.title("Carbon Footprint Reduction Dashboard")

        # Line chart showing carbon footprint reduction over time
        st.subheader("Carbon Footprint Reduction Over Time")
        fig = px.line(data, x='people', y='CO2 Emissions(g/km)', title='Carbon Footprint Reduction Over Time')
        st.plotly_chart(fig)

        # Display total number of people and total carbon footprint reduction
        total_people = data['Cylinders'].sum()
        total_reduction = data['CO2 Emissions(g/km)'].sum()
        st.subheader("Total Number of People: {}".format(total_people))
        st.subheader("Total Carbon Footprint Reduction (in tons): {}".format(total_reduction))
