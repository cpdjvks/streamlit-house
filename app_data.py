import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def run_data_app() :
    st.subheader('통합 데이터')

    tab1, tab2, tab3 = st.tabs(['전체 데이터', '평균 지역별 가격', '가장 싼 / 비싼 지역'])
    with tab1:
        st.text('단위 : 천원')
        df = pd.read_csv('./data/house.csv')
        st.dataframe(df)

    with tab2:
        st.text('단위 : 천원')
        average_prices = df.groupby('지역').mean().mean(axis=1)
        st.bar_chart(average_prices)

    with tab3:
        column_list = df.columns[1: ]
        selected_columns = st.multiselect('년월을 선택하세요', column_list)

        # 사용자가 조절 가능한 개수만큼의 지역을 표시하도록 하는 슬라이더
        num_of_areas = st.slider('표시할 지역의 개수', min_value = 1, max_value = 14, value = 1)

        # 선택한 각 년월에 대해 반복하여 처리합니다.
        for selected_column in selected_columns:
            st.text(selected_column + ' 가장 싼 지역')
            st.text('단위 : 천원')

            # 선택한 년월에 대해 월세가 싼 지역을 찾아내고, 사용자가 선택한 개수만큼 표시합니다.
            cheapest_areas = df.nsmallest(num_of_areas, selected_column)[['지역', selected_column]]
            st.dataframe(cheapest_areas)

            st.text(selected_column + ' 가장 비싼 지역')
            st.text('단위 : 천원')

            # 선택한 년월에 대해 월세가 비싼 지역을 찾아내고, 사용자가 선택한 개수만큼 표시합니다.
            most_expensive_areas = df.nlargest(num_of_areas, selected_column)[['지역', selected_column]]
            st.dataframe(most_expensive_areas)