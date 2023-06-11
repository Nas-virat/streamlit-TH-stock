import streamlit as st
import pandas as pd

import plotly.graph_objects as go
from plotly.subplots import make_subplots

from feature.metric import *
from feature.revenueProfit import *
from feature.margin import *
from feature.roeroa import *
from feature.eps import *
from feature.cashflow import *
from feature.BS import *

st.set_page_config(layout='wide', initial_sidebar_state='expanded')

with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# Load the stock data
allstock = pd.read_csv('alldata.csv')

# Get unique stock options
stock_options= allstock['Symbol'].unique()

# Create a selectbox for stock selection
selected_stock = st.sidebar.selectbox("Select a stock:",options=stock_options,index=6)
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
st.markdown('### Metrics')
metricFeature(st,filtered_data,current_year,current_quarter)

# Add space
st.markdown('<br>', unsafe_allow_html=True)

# Revenue and Profit
st.markdown('### Revenue and Profit')
revenueProfitFeature(st,filtered_data)

# Add space
st.markdown('<br>', unsafe_allow_html=True)

# Margin
st.markdown('### Gross Profit Margin and Net Profit Margin')
marginFeature(st,filtered_data)

# Add space
st.markdown('<br>', unsafe_allow_html=True)

# ROE and ROA
st.markdown('### ROE and ROA')
RoeroaFeature(st,filtered_data,current_year,current_quarter)

# Add space
st.markdown('<br>', unsafe_allow_html=True)

# EPS 
st.markdown('### Earning per Share (EPS)')
epsFeature(st,filtered_data)

# Add space
st.markdown('<br>', unsafe_allow_html=True)

# Cash Flow
st.markdown('### Cash Flow')
cashflowFeature(st,filtered_data,current_year,current_quarter)

# Balance Sheet
st.markdown('### Balance Sheet')
bsFeature(st,filtered_data,current_year,current_quarter)