import streamlit as st

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def run_trend_app() :

    st.subheader('지역별 추이')

    df = pd.read_csv('./data/house.csv')

    column_list = df.columns[1: ]

    start_column = st.text_input('시작 연월을 입력하세요(202007~202306)', min(column_list))
    end_column = st.text_input('끝 연월을 입력하세요(시작연월~202306)', max(column_list))

    # 시작열과 끝열이 데이터프레임의 열에 포함되는지 확인
    if start_column not in column_list or end_column not in column_list or start_column > end_column:
        st.warning('올바른 열 값을 입력하세요.')
        return

    # 시작열과 끝열 사이의 열을 추출
    selected_columns = [col for col in column_list if start_column <= col <= end_column]

    region_list = df['지역'].tolist()

    selected_regions = st.multiselect('지역을 선택하세요', region_list)

    if isinstance(selected_regions, str):
        selected_regions = [selected_regions]

    # 선택한 지역과 열의 데이터 추출
    selected_data = df[df['지역'].isin(selected_regions)][['지역'] + selected_columns].set_index('지역').transpose()

    st.text('단위 : 천원')

    st.line_chart(selected_data)