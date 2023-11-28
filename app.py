import streamlit as st

from app_home import run_home_app
from app_data import run_data_app
from app_trend import run_trend_app

def main() :
    st.title('전국 오피스텔 중위 월세 가격')

    menu = ['Home', '통합 데이터', '지역별 추이']

    choice = st.sidebar.selectbox('메뉴 선택', menu)

    if choice == menu[0] :
        run_home_app()
    elif choice == menu[1] :
        run_data_app()
    elif choice == menu[2] :
        run_trend_app()

if __name__ == '__main__' :
    main()