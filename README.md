# streamlit-TH-stock

![overview project img](example/All.png)

This project is apply using streamlit to build the  interactive dashboard 
for visualize the thai equity performance

## Table of Contents

- [Installation](#Installation)
- [Configuration](#Configuration)
- [Run the app](#run-the-app)
- [File and Folder Description](#File-and-Folder-Description)
- [Feature](#Feature)


# Installation
you have to install streamlit, pandas, plotly 

```bash
pip install streamlit 
pip install pandas 
pip install plotly
```

# Configuration

after the install python module,your have to make the directory of TH-stock.TH-stock folder should contain csv file in each period of time

```bash
mkdir TH-data
```
The file structure in TH-data

```
|-- TH-data
||-- 2547-Q1.csv
||-- 2547-Q2.csv
||-- 2547-Q3.csv
||-- 2547-Q4.csv
 ...
 ...
||-- 2566-Q1.csv
```

The format in each csv file the format can be show in [Example csv file](example/example.csv)
Note that the example has only 5 record stock you have to fill the data



# Run the app

To run the application run the following command in terminal

```bash
streamlit run dashboard.py
```

# File and Folder Description

1. dashboard.py
    -   This file is the main file that run the dashboard
2. setupfile.py
    -   This file setup the csv file that combine all csv file in TH-data folder.This file also clean the data into the right format
3. config folder
    -   This folder contain config color of the plot 
4. feature folder
    -   This folder contain all feature view 
5.  utils folder 
    -   This folder contain util to make a plot such as barplot,lineplot and card 



# Feature

- Balance Sheet
![BS img](example/BS.png)
- Cash Cycle
![Cash Cycle img](example/cashcycle.png)
- Cash Flow
![Cash Flow img](example/cashflow.png)
- EPS
![EPS img](example/eps.png)
- Gross Margin ,EBIT Margin , Net Margin
![Gross Margin ,EBIT Margin , Net Margin img](example/margin.png)
- Revenue and Profit
![Revenue and Profit img](example/RevenueProfit.png)
- ROE ROA
![ROE ROA img](example/ROEROA.png)
- Turnover
![Turnover img](example/Turnover.png)
 