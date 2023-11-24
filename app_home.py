import streamlit as st

def run_home_app():
    st.subheader('Home')
    st.text('전국 오피스텔의 중위 월세 가격입니다.')

    st.text('기간은 2020년 7월 부터 2023년 6월까지입니다.')

    st.text('출처 : https://www.data.go.kr/data/15048312/fileData.do')

    img_url = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTcb0GwhVYwJqb-ytwik2a301ugqKECo9S8eA&usqp=CAU'

    st.image(img_url)