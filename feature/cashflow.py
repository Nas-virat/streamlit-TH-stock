import pandas as pd
from plotly.subplots import make_subplots

from utils.utils import *
from utils.barplot import *


def cashflowFeature(st,df:pd.DataFrame,year:int,quarter:int) -> None:

    if not df.empty: 
        # Operating Cash Flow
        current_CFO = getCurrentData('Operating Cash Flow',df,year,quarter)
        # Investing Cash Flow 
        current_CFI = getCurrentData('Investing Cash Flow',df,year,quarter)
        # Financing Cash Flow
        current_CFF = getCurrentData('Financing Cash Flow',df,year,quarter)
        # Net Cash Flow
        current_NCF = getCurrentData('Net Cash Flow',df,year,quarter)

        col1, col2, col3 ,col4 = st.columns(4)
        col1.metric("Operating Cash Flow", "{:,.2f}".format(current_CFO))
        col2.metric("Investing Cash Flow", "{:,.2f}".format(current_CFI))
        col3.metric("Financing Cash Flow", "{:,.2f}".format(current_CFF))
        col4.metric("Net Cash Flow", "{:,.2f}".format(current_NCF))
        

    else:
        st.markdown('No data available for the selected stock and year range.')
        


    fig = make_subplots(specs=[[{"secondary_y": True}]])

    # Add space
    st.markdown('<br>', unsafe_allow_html=True)

    barplot(
        fig=fig,
        df=df,
        columns=['Operating Cash Flow','Investing Cash Flow','Financing Cash Flow'],
        markers=['#1f77b4','#ff7f0e','#2ca02c'],
        legendfontsize=20,
        xaxis_title='Year',
        yaxis_title='Amount',
        tickangle=-60
    )

    # Display the line plot
    st.plotly_chart(fig,use_container_width=True)


    st.markdown('### Net Cash Flow')

    fig2 = make_subplots(specs=[[{"secondary_y": True}]])

    barplot(
        fig=fig2,
        df=df,
        columns=['Net Cash Flow'],
        markers=['#1f77b4'],
        legendfontsize=20,
        xaxis_title='Year',
        yaxis_title='net cash flow',
        tickangle=-60
    )

    # Display the line plot
    st.plotly_chart(fig2,use_container_width=True)