import pandas as pd
from plotly.subplots import make_subplots

from utils.barplot import *
from utils.utils import *

def epsFeature(st,df: pd.DataFrame) -> None:

    figeps = make_subplots(specs=[[{"secondary_y": True}]])

    barplot(
        fig=figeps,
        df=df,
        columns=['EPS'],
        markers=setColor(['EPS']),
        legendfontsize=20,
        xaxis_title='Year',
        yaxis_title='Amount',
        tickangle=-60
        )

    # Display the line plot
    st.plotly_chart(figeps,use_container_width=True)