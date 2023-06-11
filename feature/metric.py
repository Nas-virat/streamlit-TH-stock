import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots

from utils.utils import * 
from utils.cardlist import *

def metricFeature(st,df:pd.DataFrame,year:int,quarter:int) -> None:
    if not df.empty: 

        cardYoY(
            st,
            columns=['Revenue','Gross Profit','EBITDA','Net Profit','EPS'],
            df=df,
            year=year,
            quarter=quarter
        )

    if df.empty:
        st.markdown('No data available for the selected stock and year range.')