import pandas as pd

import plotly.graph_objects as go
from plotly.subplots import make_subplots

def barplot(
        fig:go.Figure,
        df:pd.DataFrame,
        columns:list,
        markers:list,
        legendfontsize:int,
        xaxis_title:str,
        yaxis_title:str,
        tickangle:int,
        ) -> go.Figure | None:

    if(len(columns) != len(markers)):
        raise Exception('columns and marker must have the same length')
    
    else:
        for i in range(len(columns)):
            fig.add_trace(
                go.Bar(
                    name=columns[i],
                    x=df['Period'],
                    y=df[columns[i]],
                    base=0,
                    textposition="outside",
                    textfont=dict(size=14),
                    marker=dict(color=markers[i]) 
                ),
                secondary_y=False
            )
    
    fig.update_xaxes(tickangle=tickangle)

    fig.update_layout(
        showlegend=True,
        xaxis_title=xaxis_title,
        yaxis_title=yaxis_title,
        barmode='group',
        legend=dict(
            x=1,
            y=1,
            bgcolor='rgba(0,0,0,0)',
            font=dict(size=legendfontsize)
        )
    )

    return fig
