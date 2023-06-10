
def getCurrentData(column,df,year,quarter):
    current_temp = df[(df['Year'] == year) & (df['Quarter'] == quarter)][column].values[0]
    return current_temp

# get metric
def getmetric(column,df,year,quarter):
    current_temp = getCurrentData(column,year,quarter)
    previous_temp_list = df[(df['Year'] == year - 1) & (df['Quarter'] == quarter)][column].values
    previous_temp = round(previous_temp_list[0],2) if len(previous_temp_list) > 0 else 0
    previous_temp_yoy = (current_temp - previous_temp) / previous_temp * 100 if previous_temp != 0 else 0