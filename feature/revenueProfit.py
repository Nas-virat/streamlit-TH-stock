import pandas as pd
from plotly.subplots import make_subplots

from utils.barplot import *
from utils.utils import *

def revenueProfitFeature(st,df : pd.DataFrame) -> None:

    fig = make_subplots(specs=[[{"secondary_y": True}]])

    barplot(
        fig=fig,
        df=df,
        columns=['Revenue','EBITDA','Net Profit'],
        markers=setColor(['Revenue','EBITDA','Net Profit']),
        legendfontsize=20,
        xaxis_title='Year',
        yaxis_title='Amount',
        tickangle=-60
    )

    # Display the line plot
    st.plotly_chart(fig,use_container_width=True)
