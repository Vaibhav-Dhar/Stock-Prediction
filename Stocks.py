import streamlit as st
import yfinance as yf
import pandas as pd
import cufflinks as cf
import datetime 

# App title
st.markdown('''
# Stock Prediction App
Shown are the stock price data of Listed 500 US companies!

**Credits**
- App built by [Vaibhav Dhar]
- Built in `Python` using `streamlit`,`yfinance`, `cufflinks`, `pandas` and `datetime`
''')
st.write('---')

# Sidebar
st.sidebar.subheader('Query Parameters')
start_date = st.sidebar.date_input("Start date", datetime.date(2000, 1, 1))
end_date = st.sidebar.date_input("End date", datetime.date(2021, 10, 31))

# Retrieving tickers data
ticker_list = pd.read_csv('companies.txt')
tickerSymbol = st.sidebar.selectbox('Stock ticker', ticker_list) # Select ticker symbol
tickerData = yf.Ticker(tickerSymbol) # Get ticker data
tickerDf = tickerData.history(period='1d', start=start_date, end=end_date)

if tickerData.info['logo_url'] == "":
    string_logo = '<img src=%s width="20px" height="20px">' % "https://q2z5x2y2.rocketcdn.me/wp-content/uploads/2019/03/Chrome-Broken-Image-Icon.png"
else:
    string_logo = '<img src=%s width="20px" height="20px" >' % tickerData.info['logo_url']
st.markdown(string_logo, unsafe_allow_html=True)
string_currentPrice = tickerData.info['currentPrice']
st.info(f"Current Price = {string_currentPrice}")

string_marketCap = tickerData.info['marketCap']
st.info(f"Market Cap = {string_marketCap}")

string_grossProfits = tickerData.info['grossProfits']
st.info(f"Gross Profits = {string_grossProfits}")

string_revenuePerShare = tickerData.info['revenuePerShare']
st.info(f"Revenue Per Share = {string_revenuePerShare}")

st.header('**Ticker data**')
st.write(tickerDf)

st.header('**Linear Regression Forecast**')
qf=cf.QuantFig(tickerDf,title='First Quant Figure',legend='top',name='GS')
qf.add_bollinger_bands()
fig = qf.iplot(asFigure=True)
st.plotly_chart(fig)
