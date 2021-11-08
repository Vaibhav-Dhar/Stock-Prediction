import streamlit as st
import yfinance as yf
import pandas as pd
import cufflinks as cf
import matplotlib.pyplot as plt
import datetime

st.markdown('''
# Stock Prediction App
Shown are the stock price data of Listed companies!

**Credits**
- App built by [ Vaibhav Dhar ]
- Built in `Python` using `streamlit`,`yfinance`, `cufflinks`, `pandas` and `datetime`
''')
st.write('---')

st.sidebar.subheader('Query parameters')
start_date = st.sidebar.date_input("Start date", datetime.date(2000, 1, 1))
end_date = st.sidebar.date_input("End date", datetime.date(2021, 10, 31))


ticker_list = pd.read_csv('companies.txt')
tickerSymbol = st.sidebar.selectbox('Stock ticker', ticker_list) 
tickerData = yf.Ticker(tickerSymbol) 
tickerDf = tickerData.history(period='1d', start=start_date, end=end_date)
# tickerDf = tickerData.history(period='1w', start=start_date, end=end_date)
# tickerDf = tickerData.history(period='1m', start=start_date, end=end_date)
# tickerDf = tickerData.history(period='1y', start=start_date, end=end_date) 

string_logo = '<img src=%s>' % tickerData.info['logo_url']
st.markdown(string_logo, unsafe_allow_html=True)

# st.write(tickerData.info)

string_name = tickerData.info['longName']
st.header('**%s**' % string_name)

string_summary = tickerData.info['longBusinessSummary']
st.info(string_summary)

string_sector = tickerData.info['sector']
st.info(f"Sector = {string_sector}")

string_currentPrice = tickerData.info['currentPrice']
st.info(f"Current Price = {string_currentPrice}")

string_pegRatio = tickerData.info['pegRatio']
st.info(f"PE Ratio = {string_pegRatio}")

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

# st.subheader("Closing Price Vs Time Chart with 100MA")
# ma100 = tickerDf.close.rolling(100).mean
# qf.add_bollinger_bands()
# fig = qf.iplot(asFigure=True)
# st.plotly_chart(fig)



