import streamlit as st
import yfinance as yf
import plotly.express as px

# Page setup
st.set_page_config(page_title="Apple Stock Dashboard", page_icon="📈", layout="wide")

# Cache function to avoid re-downloading
@st.cache_data
def get_stock_data(ticker):
    """Download multiple timeframes of stock data at once."""
    return {
        "Year": yf.download(ticker, period="1y"),
        "Month": yf.download(ticker, period="1mo"),
        "2 Years": yf.download(ticker, period="2y")
    }

# Title
st.markdown(
    "<h1 style='text-align: center; color: white;'>Apple Stock Dashboard</h1>",
    unsafe_allow_html=True
)

ticker = "AAPL"

# Get all data once
all_data = get_stock_data(ticker)


choice = st.radio(
    "Select time frame",
    ["2 Years", "Year", "Month"],
    horizontal=True
)

data = all_data[choice]
data.columns = data.columns.get_level_values(0) #I have this to remove the AAPL column name from each of the columns (close, low, high, etc.). yfinance adds the ticker name to each of the columns unfortunately.



fig = px.line(data, x=data.index, y='Close', title="AAPL Close Price")
fig.update_layout(
    xaxis_title="Date",
    yaxis_title="Close Price",
    hovermode="x unified",
    dragmode=False
)

# Show chart
st.plotly_chart(fig, use_container_width=True, config={"displayModeBar": False})
