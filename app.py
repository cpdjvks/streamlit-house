import streamlit as st

from app_home import run_home_app


def main() :
    st.title('전국 오피스텔 월세 가격')

    menu = ['Home', 'eda']

    choice = st.sidebar.selectbox('메뉴 선택', menu)

    if choice == menu[0] :
        run_home_app
    elif choice == menu[1] :
        run_eda_app()

if __name__ == '__main__' :
    main()