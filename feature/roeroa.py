import streamlit as st
import pandas as pd

import plotly.graph_objects as go
from plotly.subplots import make_subplots

from utils.utils import * 


def RoeroaFeature(st,filtered_data : pd.DataFrame,year:int,quarter:int):

    # show line plots
    st.markdown('### ROE and ROA')

    if filtered_data.empty:
        st.markdown('No data available for the selected stock and year range.')
    else:
        # Display the metrics
        #ROE ROA
        roe = getCurrentData('ROE',filtered_data,year,quarter)
        roa = getCurrentData('ROA',filtered_data,year,quarter)
        de = getCurrentData('D/E',filtered_data,year,quarter)

        
        col1, col2, col3 = st.columns(3)
        col1.metric("Return on Equity (ROE)", "{:,.2f}".format(roe))
        col2.metric("Return on Asset (ROA)", "{:,.2f}".format(roa))
        col3.metric("Debt to Equity", "{:,.2f}".format(de))


    figroeroa = make_subplots(specs=[[{"secondary_y": True}]])

    figroeroa.add_trace(
        go.Scatter(
            mode="lines+markers+text",
            name='ROA',
            x=filtered_data['Period'],
            y=filtered_data['ROA'],
            textposition="top center",
            textfont=dict(size=14),
            marker=dict(color='#d62728')
        ),
        secondary_y=False
    )

    figroeroa.add_trace(
        go.Scatter(
            mode="lines+markers+text",
            name='ROE',
            x=filtered_data['Period'],
            y=filtered_data['ROE'],
            textposition="top center",
            textfont=dict(size=14),
            marker=dict(color='#2ca02c') 
        ),
        secondary_y=False
    )

    figroeroa.update_layout(
        xaxis_title='Year',
        yaxis_title='Amount',
        barmode='group',
        legend=dict(
            x=1,
            y=1,
            bgcolor='rgba(0,0,0,0)',
            bordercolor='rgba(0,0,0,0)',
            font=dict(
                size=20
            )
        )
    )
    # Update x-axis labels rotation
    figroeroa.update_xaxes(tickangle=-60)

    # Display the line plot
    st.plotly_chart(figroeroa,use_container_width=True)
