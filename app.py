import streamlit as st

from app_home import run_home_app
from app_matrix import run_matrix_app
from app_chart import run_chart_app


def main() :
    st.title('전국 오피스텔 중위 월세 가격')

    menu = ['Home', '표 데이터', '차트 데이터']

    choice = st.sidebar.selectbox('메뉴 선택', menu)

    if choice == menu[0] :
        run_home_app()
    elif choice == menu[1] :
        run_matrix_app()
    elif choice == menu[2] :
        run_chart_app()

if __name__ == '__main__' :
    main()