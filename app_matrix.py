import streamlit as st

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def run_matrix_app() :

    st.subheader('표 데이터')

    tab1, tab2 = st.tabs(['전체 데이터' , '가장 싼 / 비싼 지역'])

    with tab1:
        st.text('단위 : 천원')
        df = pd.read_csv('./data/house.csv')
        st.dataframe(df)

    with tab2:
        column_list = df.columns[1: ]
        selected_column = st.selectbox('년월을 선택하세요', column_list)

        st.text(selected_column + ' 가장 싼 지역')
        st.text('단위 : 천원')
        st.dataframe(df.loc[df[selected_column] == df[selected_column].min(), ])

        st.text(selected_column + ' 가장 비싼 지역')
        st.text('단위 : 천원')
        st.dataframe(df.loc[df[selected_column] == df[selected_column].max(), ])