import pandas as pd
from plotly.subplots import make_subplots

from utils.utils import *
from utils.barplot import *
from utils.cardlist import *

def bsFeature(st,df:pd.DataFrame,year:int,quarter:int) -> None:

    if not df.empty: 

        cardYoY(
            st,
            columns=['Total Asset','Total Liabilities','Equity','D/E'],
            df=df,
            year=year,
            quarter=quarter
        )


    # Add space
    st.markdown('<br>', unsafe_allow_html=True)

    fig = make_subplots(specs=[[{"secondary_y": True}]])
    barplot(
        fig=fig,
        df=df,
        columns=['Total Asset','Total Liabilities','Equity'],
        markers=setColor(['Total Asset','Total Liabilities','Equity']),
        legendfontsize=20,
        xaxis_title='Year',
        yaxis_title='Amount',
        tickangle=-60
    )

    # Display the line plot
    st.plotly_chart(fig,use_container_width=True)

    st.markdown('### Paid-up Cap')

    fig2 = make_subplots(specs=[[{"secondary_y": True}]])
    barplot(
        fig=fig2,
        df=df,
        columns=['Paid-up Cap'],
        markers=setColor(['Paid-up Cap']),
        legendfontsize=20,
        xaxis_title='Year',
        yaxis_title='Amount',
        tickangle=-60
    )

    # Display the line plot
    st.plotly_chart(fig2,use_container_width=True)

    if df.empty:
        st.markdown('No data available for the selected stock and year range.')

    
