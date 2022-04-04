import streamlit as st
import osayu.osayu
import tetu.tetu


def main():
    st.write('ここで変更できます')
    choose = st.selectbox('', ('おさゆ', 'てっさん'), )

    if choose == 'おさゆ':
        osayu.osayu.render()
    elif choose == 'てっさん':
        tetu.tetu.render()


if __name__ == '__main__':
    main()
