import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots

from utils.utils import * 

def metricFeature(st,filtered_data:pd.DataFrame,year:int,quarter:int):
    if not filtered_data.empty: 

        # Revenue
        current_revenue,previous_revenue_yoy  = getmetric('Revenue',filtered_data,year,quarter)

        # Gross Profit 
        current_gp,previous_gp_yoy  = getmetric('Gross Profit',filtered_data,year,quarter)

        # EBITDA
        current_ebitda,previous_ebitda_yoy  = getmetric('EBITDA',filtered_data,year,quarter)

        # Net profit
        current_np,previous_np_yoy = getmetric('Net Profit',filtered_data,year,quarter)

        #EPS
        current_eps,previous_eps_yoy = getmetric('EPS',filtered_data,year,quarter)


    # show Metrics
    st.markdown('### Metrics')

    # Add space
    st.markdown('<br>', unsafe_allow_html=True)

    if filtered_data.empty:
        st.markdown('No data available for the selected stock and year range.')
    else:
        # Display the metrics
        col1, col2, col3, col4, col5 = st.columns(5)
        col1.metric("Revenue", "{:,.2f}".format(current_revenue), f"{previous_revenue_yoy:.2f}"+"% YoY")
        col2.metric("Gross Profit", "{:,.2f}".format(current_gp), f"{previous_gp_yoy:.2f}"+"% YoY")
        col3.metric("EBITDA", "{:,.2f}".format(current_ebitda), f"{previous_ebitda_yoy:.2f}"+"% YoY")
        col4.metric("Net Profit", "{:,.2f}".format(current_np), f"{previous_np_yoy:.2f}"+"% YoY")
        col5.metric("EPS", "{:,.2f}".format(current_eps), f"{previous_eps_yoy:.2f}"+"% YoY")