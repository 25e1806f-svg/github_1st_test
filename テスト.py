import streamlit as st

st.title('初めてのアコム')
st.write('これから作品をつくっていきます。')

text = st.text_input('あなたの名前を教えてください')
st.write('あなたの名前は、' + text + 'です')

condition = st.slider('あなたの今の調子は？',0,100,50)
                                           #最小値,最大値,スタート位置
st.write('コンディション：',condition)

option = st.selectbox('好きな数字を教えてください',list(['1番','2番','3番','4番']))
st.write('あなたが選択したのは,'+ option +'です')

left_column,right_column = st.columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここは右カラムです')

from PIL import Image #PILをpip install pillowを実施する
img = Image.open('えいご.png')
            #自分の画像のファイル名にする(room.jpgは例えば)
            #自分のPCの画像を同じフォルダに入れて指定する
st.image(img,caption = '生活場面', use_column_width=True) 

import pandas as pd
import numpy as np
df = pd.DataFrame(np.random.rand(100,2)/[50,50]+[36.64,138.19],columns = ['lat','lon']) #lat lon 緯度　経度

#緯度と経度から地図に書き込む
st.map(df)
st.table(df)

st.bar_chart(df)

import streamlit as st
from openai import OpenAI

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

st.title("AI質問アプリ")

question = st.text_input("質問を入力してください")

if st.button("AIに質問する"):
    response = client.responses.create(
        model="gpt-5.6",
        input=question
    )

    st.write(response.output_text)