
import pandas as pd
from plotly.subplots import make_subplots

from utils.utils import * 
from utils.lineplot import *
from utils.cardlist import *

def RoeroaFeature(st,df : pd.DataFrame,year:int,quarter:int) -> None:

    if df.empty:
        st.markdown('No data available for the selected stock and year range.')
    else:
        card(
            st,
            columns=['ROE','ROA','D/E'],
            df=df,
            year=year,
            quarter=quarter
        )

    fig = make_subplots(specs=[[{"secondary_y": True}]])

    lineplot(
        fig=fig,
        df=df,
        columns=['ROE','ROA'],
        markers=['#2ca02c','#d62728'],
        legendfontsize=20,
        xaxis_title='Year',
        yaxis_title='Amount',
        tickangle=-60
    )

    # Display the line plot
    st.plotly_chart(fig,use_container_width=True)
