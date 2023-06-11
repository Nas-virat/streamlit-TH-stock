import pandas as pd
from plotly.subplots import make_subplots

from utils.utils import *
from utils.barplot import *

def bsFeature(st,df:pd.DataFrame,year:int,quarter:int) -> None:

    if not df.empty: 

        # Total Asset
        current_TA,previous_TA_yoy  = getmetric('Total Asset',df,year,quarter)

        # Totla Liabilities 
        current_TL,previous_TL_yoy  = getmetric('Total Liabilities',df,year,quarter)

        # Equity
        current_Equity,previous_Equity_yoy  = getmetric('Equity',df,year,quarter)

        # Display the metrics
        col1, col2, col3 = st.columns(3)
        col1.metric("Total Asset", "{:,.2f}".format(current_TA), f"{previous_TA_yoy:.2f}"+"% YoY")
        col2.metric("Total Liabilities", "{:,.2f}".format(current_TL), f"{previous_TL_yoy:.2f}"+"% YoY")
        col3.metric("Equity", "{:,.2f}".format(current_Equity), f"{previous_Equity_yoy:.2f}"+"% YoY")
        
    # Add space
    st.markdown('<br>', unsafe_allow_html=True)

    fig = make_subplots(specs=[[{"secondary_y": True}]])
    barplot(
        fig=fig,
        df=df,
        columns=['Total Asset','Total Liabilities','Equity'],
        markers=['#2ca02c','#ff7f0e','#d62728'],
        legendfontsize=20,
        xaxis_title='Year',
        yaxis_title='Amount',
        tickangle=-60
    )

    # Display the line plot
    st.plotly_chart(fig,use_container_width=True)

    if df.empty:
        st.markdown('No data available for the selected stock and year range.')

    
