import streamlit as st

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def run_eda_app() :

    st.subheader('전체 데이터')

    st.text('단위 : 천원')

    df = pd.read_csv('./data/house.csv')

    st.dataframe(df)

    column_list = df.columns[1: ]

    selected_column = st.selectbox('년월을 선택하세요', column_list)

    st.text(selected_column + ' 가장 싼 지역')
    st.dataframe(df.loc[df[selected_column] == df[selected_column].min(), ])

    st.text(selected_column + ' 가장 비싼 지역')
    st.dataframe(df.loc[df[selected_column] == df[selected_column].max(), ])

    st.dataframe(df.loc[0,])