import requests
import pandas as pd
import streamlit as st
import datetime as dt


def get_stock_price(code, startdate, enddate) :
  url = "https://m.stock.naver.com/front-api/external/chart/domestic/info?symbol={}&requestType=1&startTime={}&endTime={}&timeframe=day".format(code, startdate, enddate)
  rq = requests.get(url)
  li = eval(rq.text.replace("\n","").replace("\t",""))

  return pd.DataFrame(columns=li[0], data=li[1:])


st.set_page_config(page_title='주식차트', page_icon=':coffee:')
st.title('주식차트')



startdate = st.date_input(
  "조회 시작일을 선택해 주세요.",
  dt.datetime(2024, 1, 1)
)

enddate = st.date_input(
  "조회 마지막 일을 선택해 주세요."
)

code = st.text_input(
  "종목코드를 입력해주세요."
)

if startdate and enddate and code :
  df = get_stock_price(code, startdate.strftime('%Y%m%d'), enddate.strftime('%Y%m%d'))

  st.dataframe(df)
  st.line_chart(df['종가'])
  st.bar_chart(df['거래량'])

