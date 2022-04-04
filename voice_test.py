import streamlit as st

audio_file = open('../tetu.wav', 'rb')
audio_bytes = audio_file.read()

st.audio(audio_bytes, format='audio/ogg')
