
import pandas as pd
from plotly.subplots import make_subplots

from utils.utils import * 
from utils.lineplot import *


def RoeroaFeature(st,df : pd.DataFrame,year:int,quarter:int) -> None:

    if df.empty:
        st.markdown('No data available for the selected stock and year range.')
    else:
        # Display the metrics
        #ROE ROA
        roe = getCurrentData('ROE',df,year,quarter)
        roa = getCurrentData('ROA',df,year,quarter)
        de = getCurrentData('D/E',df,year,quarter)

        
        col1, col2, col3 = st.columns(3)
        col1.metric("Return on Equity (ROE)", "{:,.2f}".format(roe))
        col2.metric("Return on Asset (ROA)", "{:,.2f}".format(roa))
        col3.metric("Debt to Equity", "{:,.2f}".format(de))


    figroeroa = make_subplots(specs=[[{"secondary_y": True}]])

    lineplot(
        fig=figroeroa,
        df=df,
        columns=['ROE','ROA'],
        markers=['#2ca02c','#d62728'],
        legendfontsize=20,
        xaxis_title='Year',
        yaxis_title='Amount',
        tickangle=-60
    )

    # Display the line plot
    st.plotly_chart(figroeroa,use_container_width=True)
