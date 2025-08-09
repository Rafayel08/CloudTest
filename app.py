import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf
from streamlit_autorefresh import st_autorefresh

st_autorefresh(interval=60 * 1000, key="auto_refresh")

stock = yf.Ticker("AAPL")

#dataframe
df = stock.history(period="1y")



# Create figure and axes
fig = plt.figure(figsize=(8, 5))
ax = fig.add_subplot(1, 1, 1)

# Plot on the axes
ax.plot(df.index, df['Close'])
ax.set_title('Close Prices')
ax.set_xlabel('Date')
ax.set_ylabel('Price')
ax.grid(True)

st.pyplot(fig)
