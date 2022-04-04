import streamlit as st
import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# スライドバー
st.sidebar.title('GAFA株価')
st.sidebar.write('こちらは株価可視化ツールです。以下のオプションから表示日数を設定できます。')
# 期間選択
st.sidebar.header('表示日数選択')
days = st.sidebar.slider('日数', 1, 50, 20)

# 株価の範囲選択
st.sidebar.header('株価の範囲指定')
ymin, ymax = st.sidebar.slider(
        '範囲を指定してください。',
        0.0, 3500.0, (0.0, 3500.0)
)

# メイン画面
st.title('米国株価可視化アプリ')

st.subheader(f'過去{days}日間のGAFAの株価')

options = st.multiselect(
     '会社名を選択してください。',
     ['google', 'amazon', 'facebook', 'apple', 'microsoft', 'netflix'],
     ['google', 'amazon', 'facebook', 'apple', 'microsoft', 'netflix'])

tickers = {
        'apple': 'AAPL',
        'facebook': 'FB',
        'google': 'GOOGL',
        'microsoft': 'MSFT',
        'netflix': 'NFLX',
        'amazon': 'AMZN'
}

st.subheader('株価(USD)')

df = pd.DataFrame()
for company in tickers.keys():
    if company in options:
        tkr = yf.Ticker(tickers[company])
        hist = tkr.history(period=f'{days}d')
        hist.index = hist.index.strftime('%d %B %Y')
        hist = hist[['Close']]
        hist.columns = [company]
        hist = hist.T
        hist.index.name = 'Name'
        df = pd.concat([df, hist])

st.write(df)

chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])

st.line_chart(chart_data)
