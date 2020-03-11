import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import time
import os

df=pd.read_csv('/home/shobha/Desktop/PYTHON_BASICS/AK/corona virus.csv')
df.head(10)
countries=df.drop('Date',axis=1)
def plot_growth(dates,country):
    plt.rcParams['figure.figsize']=(20,10)
    plt.plot_date(dates,country)
    plt.xlabel("Date",fontsize=18)
    plt.ylabel("Infected people",fontsize=16)

    for country in countries.columns:
        plot_growth(df['Date'], df[country])

for country in countries.columns:
    fig=px.pie(df,values=country,names='Date',title=f'Count Infected {country}')
    fig.show()
    time.sleep(10)