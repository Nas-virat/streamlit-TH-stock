import pandas as pd
from plotly.subplots import make_subplots

from utils.utils import *
from utils.cardlist import *
from utils.lineplot import *

def cashCyclefeature(st,df:pd.DataFrame,year:int,quarter:int) -> None:

    if not df.empty: 
        card(
            st,
            columns=['Average Sale Period',
                     'Average Collection Period',
                     'Average Payment Period',
                     'Cash Cycle'
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
        columns=['Average Sale Period','Average Collection Period','Average Payment Period'],
        markers=setColor(['Average Sale Period','Average Collection Period','Average Payment Period']),
        legendfontsize=20,
        xaxis_title='Year',
        yaxis_title='Days',
        tickangle=-60
    )

    # Display the line plot
    st.plotly_chart(fig,use_container_width=True)
