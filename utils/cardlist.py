
from utils.utils import *

def card(st,columns:list,df,year,quarter)-> None:

    list_metrics = []

    for column in columns:
        list_metrics.append(getCurrentData(column,df,year,quarter))


    col = st.columns(list_metrics.__len__())


    for i in range(list_metrics.__len__()):
        col[i].metric(columns[i], "{:,.2f}".format(list_metrics[i]))
    