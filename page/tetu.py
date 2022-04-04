import streamlit as st
# from pathlib import Path
import os


def render():
    st.title('てっさんボイス')
    path = '../tetu'
    files = []
    for filename in os.listdir(path):
        if os.path.isfile(os.path.join(path, filename)):  # ファイルのみ取得
            files.append(filename)
    for file in files:
        name = os.path.splitext(os.path.basename(file))[0]
        audio_file = open(file, 'rb')
        audio_bytes = audio_file.read()
        st.write(name)
        st.audio(audio_bytes, format='audio/ogg')
