import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots

def revenueProfitFeature(st,filtered_data : pd.DataFrame):
    # show Metrics
    st.markdown('### Revenue and Profit')

    fig = make_subplots(specs=[[{"secondary_y": True}]])

    # Add revenue bar
    fig.add_trace(
        go.Bar(
            name='Revenue',
            x=filtered_data['Period'],
            y=filtered_data['Revenue'],
            base=0,
            textposition="outside",
            textfont=dict(size=14),
            marker=dict(color='#1f77b4') 
        ),
        secondary_y=False
    )
    # Add EBITDA bar
    fig.add_trace(
        go.Bar(
            name='EBITDA',
            x=filtered_data['Period'],
            y=filtered_data['EBITDA'],
            base=0,
            textposition="outside",
            textfont=dict(size=14),
            marker=dict(color='#ff7f0e')
        ),
        secondary_y=False
    )
    # Add revenue bar
    fig.add_trace(
        go.Bar(
            name='Net Profit',
            x=filtered_data['Period'],
            y=filtered_data['Net Profit'],
            base=0,
            textposition="outside",
            textfont=dict(size=14),
            marker=dict(color='#2ca02c')
        ),
        secondary_y=False
    )

    # Update x-axis labels rotation
    fig.update_xaxes(tickangle=-60)


    fig.update_layout(
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

    # Display the line plot
    st.plotly_chart(fig,use_container_width=True)
