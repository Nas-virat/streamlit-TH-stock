import pandas as pd
from utils.utils import *

def card(
         st,
         columns:list[str],
         df: pd.DataFrame,
         year: int,
         quarter: int
        )-> None:

    list_metrics = []

    for column in columns:
        list_metrics.append(getCurrentData(column,df,year,quarter))


    col = st.columns(list_metrics.__len__())


    for i in range(list_metrics.__len__()):
        col[i].metric(columns[i], "{:,.2f}".format(list_metrics[i]))

def cardYoY(
         st,
         columns:list[str],
         df: pd.DataFrame,
         year: int,
         quarter: int
        )-> None:

    list_metrics = []

    for column in columns:
        list_metrics.append(getmetric(column,df,year,quarter))


    col = st.columns(list_metrics.__len__())


    for i in range(list_metrics.__len__()):
        col[i].metric(columns[i], "{:,.2f}".format(list_metrics[i][0]), f"{list_metrics[i][1]:.2f}"+"% YoY")
    