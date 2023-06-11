import pandas as pd
from plotly.subplots import make_subplots

from utils.utils import *
from utils.cardlist import *
from utils.lineplot import *

def turnOverfeature(st,df:pd.DataFrame,year:int,quarter:int) -> None:

    if not df.empty: 
        card(
            st,
            columns=['Total Asset Turnover',
                     'Inventory Turnover',
                     'Accounts Receivable Turnover',
                     'Account Payable Turnover'
                     ],
            df=df,
            year=year,
            quarter=quarter
        )

    else:
        st.markdown('No data available for the selected stock and year range.')

    fig = make_subplots(specs=[[{"secondary_y": True}]])

    lineplot(
        fig=fig,
        df=df,
        columns=['Total Asset Turnover','Inventory Turnover','Accounts Receivable Turnover','Account Payable Turnover'],
        markers=setColor(['Total Asset Turnover','Inventory Turnover','Accounts Receivable Turnover','Account Payable Turnover']),
        legendfontsize=20,
        xaxis_title='Year',
        yaxis_title='Days',
        tickangle=-60
    )

    # Display the line plot
    st.plotly_chart(fig,use_container_width=True)