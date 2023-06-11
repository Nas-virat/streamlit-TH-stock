import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots

from utils.lineplot import *
from utils.utils import *

def marginFeature(st,df : pd.DataFrame) -> None:

    figline = make_subplots(specs=[[{"secondary_y": True}]])

    lineplot(
        fig=figline,
        df=df,
        columns=['Gross Profit Margin','EBIT Margin','Net Profit Margin'],
        markers=setColor(['Gross Profit Margin','EBIT Margin','Net Profit Margin']),
        legendfontsize=20,
        xaxis_title='Year',
        yaxis_title='Amount',
        tickangle=-60
    )

    # Display the line plot
    st.plotly_chart(figline,use_container_width=True)

