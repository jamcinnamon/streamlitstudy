import streamlit as st
import pandas as pd
import numpy as np
import requests
import json
import seaborn as sns

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY':'9367716d-9a17-4b26-88c7-078e75477cea',
}

parameter1 = {
  'start':'1',
  'limit':'20',
  'convert':'USD',
  'sort': 'market_cap',
  'sort_dir': 'desc',
}

parameter2 = {
  'start':'21',
  'limit':'40',
  'convert':'USD',
  'sort': 'market_cap',
  'sort_dir': 'desc',
  'price_max': '100'
}

response = requests.get(url, headers=headers, params=parameter1)
data = response.json()
response_2 = requests.get(url, headers=headers, params=parameter2)
data_2 = response.json()

datas = data['data']+data_2['data']

df = pd.json_normalize(datas)

st.title('coin market')

if st.button("Home"):
    st.switch_page("main.py")
if st.button("Chart Page"):
    st.switch_page("pages/page1.py")
if st.button("Looking For Your Coin"):
    st.switch_page("pages/page2.py")
with st.container():
  st.write("한눈에 보는 7일 동안 코인 변동률")
  sns.set_theme(style="whitegrid")
  sns.barplot(x='symbol', y='quote.USD.percent_change_7d', data=pd.json_normalize(datas))
