import streamlit as st
import pandas as pd

import plotly.graph_objects as go
from plotly.subplots import make_subplots

from feature.eps import *
from feature.margin import *
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

# Calculate the YoY metric 
current_year = filtered_data['Year'].max()
previous_year = current_year - 1
current_quarter = filtered_data[filtered_data['Year'] == current_year]['Quarter'].max()


def getCurrentData(column):
    current_temp = filtered_data[(filtered_data['Year'] == current_year) & (filtered_data['Quarter'] == current_quarter)][column].values[0]
    return current_temp

# get metric
def getmetric(column):
    current_temp = getCurrentData(column)
    previous_temp_list = filtered_data[(filtered_data['Year'] == previous_year) & (filtered_data['Quarter'] == current_quarter)][column].values
    previous_temp = round(previous_temp_list[0],2) if len(previous_temp_list) > 0 else 0
    previous_temp_yoy = (current_temp - previous_temp) / previous_temp * 100 if previous_temp != 0 else 0

    return current_temp , previous_temp_yoy


if not filtered_data.empty: 

    # Revenue
    current_revenue,previous_revenue_yoy  = getmetric('Revenue')

    # Gross Profit 
    current_gp,previous_gp_yoy  = getmetric('Gross Profit')

    # EBITDA
    current_ebitda,previous_ebitda_yoy  = getmetric('EBITDA')

    # Net profit
    current_np,previous_np_yoy = getmetric('Net Profit')

    #EPS
    current_eps,previous_eps_yoy = getmetric('EPS')


# show Metrics
st.markdown('### Metrics')

# Add space
st.markdown('<br>', unsafe_allow_html=True)

if filtered_data.empty:
    st.markdown('No data available for the selected stock and year range.')
else:
    # Display the metrics
    col1, col2, col3, col4, col5 = st.columns(5)
    col1.metric("Revenue", "{:,.2f}".format(current_revenue), f"{previous_revenue_yoy:.2f}"+"% YoY")
    col2.metric("Gross Profit", "{:,.2f}".format(current_gp), f"{previous_gp_yoy:.2f}"+"% YoY")
    col3.metric("EBITDA", "{:,.2f}".format(current_ebitda), f"{previous_ebitda_yoy:.2f}"+"% YoY")
    col4.metric("Net Profit", "{:,.2f}".format(current_np), f"{previous_np_yoy:.2f}"+"% YoY")
    col5.metric("EPS", "{:,.2f}".format(current_eps), f"{previous_eps_yoy:.2f}"+"% YoY")



revenueProfitFeature(st,filtered_data)

# Add space
st.markdown('<br>', unsafe_allow_html=True)

marginFeature(st,filtered_data)

# Add space
st.markdown('<br>', unsafe_allow_html=True)

# ROE and ROA
RoeroaFeature(st,filtered_data,current_year,current_quarter)

# Add space
st.markdown('<br>', unsafe_allow_html=True)

# EPS 
epsFeature(st,filtered_data)