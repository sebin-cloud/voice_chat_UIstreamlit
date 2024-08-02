# 실행방법
# stramlit run 0streamlit_test.py
import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

#pandas : 2차원 데이터로 db를 저장하고 전처리,시각화할 때 사용할 수 있는 라이브러리
#random : rand : 행&렬 -> 데이터프레임을 만든 것 
chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])
print(chart_data)

c = (
   alt.Chart(chart_data)
   .mark_circle()
   .encode(x="a", y="b", size="c", color="c", tooltip=["a", "b", "c"])
)

st.altair_chart(c, use_container_width=True)
















