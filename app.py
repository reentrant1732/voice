import streamlit as st
import osayu
import tetu


def main():
    with st.sidebar:
        'ここで変更できます'
        page = st.selectbox('', ('おさゆ', 'てっさん'), )

    if page == 'おさゆ':
        osayu.render()
    elif page == 'てっさん':
        tetu.render()


if __name__ == '__main__':
    main()