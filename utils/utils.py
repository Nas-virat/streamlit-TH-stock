import pandas as pd 
from config.color import *
def getCurrentData(
        column:str,
        df: pd.DataFrame,
        year:int,
        quarter:int
        ) -> float:
    current_temp = df[(df['Year'] == year) & (df['Quarter'] == quarter)][column].values[0]
    return current_temp

# get metric
def getmetric(
        column:str,
        df: pd.DataFrame,
        year:int,
        quarter:int
        ) -> tuple:
    current_temp = getCurrentData(column,df,year,quarter)
    previous_temp_list = df[(df['Year'] == year - 1) & (df['Quarter'] == quarter)][column].values
    previous_temp = round(previous_temp_list[0],2) if len(previous_temp_list) > 0 else 0
    previous_temp_yoy = (current_temp - previous_temp) / previous_temp * 100 if previous_temp != 0 else 0
    previous_temp_yoy = previous_temp_yoy if previous_temp >= 0 else -previous_temp_yoy

    return current_temp , previous_temp_yoy

def setColor(columns:list[str]) -> list[str]:
    list_color = []
    for column in columns:
        list_color.append(Color[column])
    return list_color
