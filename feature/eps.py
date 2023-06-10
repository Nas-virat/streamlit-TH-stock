import streamlit as st
import pandas as pd

import plotly.graph_objects as go
from plotly.subplots import make_subplots



def epsFeature(st,filtered_data : pd.DataFrame):
    # EPS 

    # show line plots
    st.markdown('### Earning per Share (EPS)')

    figeps = make_subplots(specs=[[{"secondary_y": True}]])

    figeps.add_trace(
        go.Bar(
            name='EPS',
            x=filtered_data['Period'],
            y=filtered_data['EPS'],
            base=0,
            textposition="outside",
            textfont=dict(size=14),
            marker=dict(color='#2ca02c')
        ),
        secondary_y=False
    )

    figeps.update_layout(
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
    figeps.update_xaxes(tickangle=-60)

    # Display the line plot
    st.plotly_chart(figeps,use_container_width=True)