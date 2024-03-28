import streamlit as st
import pandas as pd
import plotly.express as px


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
