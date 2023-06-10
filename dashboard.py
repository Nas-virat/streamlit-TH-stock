import streamlit as st
import pandas as pd

import plotly.graph_objects as go
from plotly.subplots import make_subplots

from feature.eps import *
from feature.margin import *
from feature.metric import *
from feature.revenueProfit import *
from feature.roeroa import *

st.set_page_config(layout='wide', initial_sidebar_state='expanded')

with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# Load the stock data
allstock = pd.read_csv('alldata.csv')

# Get unique stock options
stock_options= allstock['Symbol'].unique()



# Create a selectbox for stock selection
selected_stock = st.sidebar.selectbox("Select a stock:",stock_options)
st.sidebar.subheader('Range of year')

min_year = allstock['Year'].min()
max_year = allstock['Year'].max()

range = st.sidebar.slider(
    'Select a range of year',
    min_value=2547,
    max_value=int(max_year),
    value=[int(max_year-10),int(max_year)]
)


# Title of the Website
st.title(selected_stock)

# Add space
st.markdown('<br>', unsafe_allow_html=True)

# Filter data based in the selected stock and range
filtered_data = allstock[(allstock['Symbol'] == selected_stock) & (allstock['Year'] >= range[0]) & (allstock['Year'] <= range[1])]

# Sort the filtered data table
filtered_data = filtered_data.sort_values(by=['Year','Quarter'])

# Calculate current year and quarter from csv file
current_year = filtered_data['Year'].max()

current_quarter = filtered_data[filtered_data['Year'] == current_year]['Quarter'].max()


#Metric Feature
metricFeature(st,filtered_data,current_year,current_quarter)

# Add space
st.markdown('<br>', unsafe_allow_html=True)

revenueProfitFeature(st,filtered_data)

# Add space
st.markdown('<br>', unsafe_allow_html=True)

# Margin
marginFeature(st,filtered_data)

# Add space
st.markdown('<br>', unsafe_allow_html=True)

# ROE and ROA
RoeroaFeature(st,filtered_data,current_year,current_quarter)

# Add space
st.markdown('<br>', unsafe_allow_html=True)

# EPS 
epsFeature(st,filtered_data)