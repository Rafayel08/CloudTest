import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf
from streamlit_autorefresh import st_autorefresh
import numpy as np
import plotly.express as px

st_autorefresh(interval=60 * 5 * 1000, key="auto_refresh")

stock = yf.Ticker("AAPL")

#dataframe
df = stock.history(period="1y")



#create Plotly figure
fig = px.line(df, x=df.index, y="Close", title="AAPL Close Price")
fig.update_layout(
    xaxis_title="Date",
    yaxis_title="Close Price",
    hovermode="x unified",
    height = 600,
    width = 1800
)

#display in Streamlit
st.plotly_chart(fig)
