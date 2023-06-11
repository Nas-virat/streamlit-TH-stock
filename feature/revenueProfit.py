import pandas as pd
from plotly.subplots import make_subplots

from utils.barplot import *

def revenueProfitFeature(st,df : pd.DataFrame) -> None:

    fig = make_subplots(specs=[[{"secondary_y": True}]])

    barplot(
        fig=fig,
        df=df,
        columns=['Revenue','EBITDA','Net Profit'],
        markers=['#1f77b4','#ff7f0e','#2ca02c'],
        legendfontsize=20,
        xaxis_title='Year',
        yaxis_title='Amount',
        tickangle=-60
    )

    # Display the line plot
    st.plotly_chart(fig,use_container_width=True)
