import streamlit as st
# from pathlib import Path
import os
import glob


def render():
    st.title('てっさんボイス')
    pathlist = glob.glob('**/*.wav')
    for file in pathlist:
        name = os.path.splitext(os.path.basename(file))[0]
        name = name.replace('.O', '')
        audio_file = open(file, 'rb')
        audio_bytes = audio_file.read()
        st.write(name)
        st.audio(audio_bytes, format='audio/ogg')
