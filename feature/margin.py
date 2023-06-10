import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots

def marginFeature(st,filtered_data : pd.DataFrame):
    # show line plots
    st.markdown('### Gross Profit Margin and Net Profit Margin')

    figline = make_subplots(specs=[[{"secondary_y": True}]])

    figline.add_trace(
        go.Scatter(
            mode="lines+markers+text",
            name='Gross Profit Margin',
            x=filtered_data['Period'],
            y=filtered_data['Gross Profit Margin'],
            textposition="top center",
            textfont=dict(size=14),
            marker=dict(color='#d62728')
        ),
        secondary_y=False
    )

    figline.add_trace(
        go.Scatter(
            mode="lines+markers+text",
            name='Net Profit Margin',
            x=filtered_data['Period'],
            y=filtered_data['Net Profit Margin'],
            textposition="top center",
            textfont=dict(size=14),
            marker=dict(color='#2ca02c') 
        ),
        secondary_y=False
    )

    figline.update_layout(
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
    figline.update_xaxes(tickangle=-60)

    # Display the line plot
    st.plotly_chart(figline,use_container_width=True)

