import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web

style.use('ggplot')

# Fetching data from yahoo
# start = dt.datetime(2000, 1, 1)
# end = dt.datetime(2019, 12, 31)
#
# df = web.DataReader('TSLA', 'yahoo', start, end)
#print(df.head())
#print(len(df))

# Convert dataframe to csv
# df.to_csv('tesla.csv')

# Reading csv file from
df = pd.read_csv('tesla.csv', parse_dates=True, index_col=0)
print(df[['Open', 'High']].head())

df['Adj Close'].plot()
plt.show()
