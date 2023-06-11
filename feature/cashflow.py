import pandas as pd
from plotly.subplots import make_subplots

from utils.utils import *
from utils.barplot import *
from utils.cardlist import *


def cashflowFeature(st,df:pd.DataFrame,year:int,quarter:int) -> None:

    if not df.empty: 
        card(
            st,
            columns=['Operating Cash Flow',
                     'Investing Cash Flow',
                     'Financing Cash Flow',
                     'Net Cash Flow'
                     ],
            df=df,
            year=year,
            quarter=quarter
        )

    else:
        st.markdown('No data available for the selected stock and year range.')
        


    fig = make_subplots(specs=[[{"secondary_y": True}]])

    # Add space
    st.markdown('<br>', unsafe_allow_html=True)

    barplot(
        fig=fig,
        df=df,
        columns=['Operating Cash Flow','Investing Cash Flow','Financing Cash Flow'],
        markers=setColor(['Operating Cash Flow','Investing Cash Flow','Financing Cash Flow']),
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