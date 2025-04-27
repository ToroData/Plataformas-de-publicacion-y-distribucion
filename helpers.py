import streamlit as st
import requests

def set_img(url, caption_img, subheader_img=None):
    if subheader_img:
        st.subheader(subheader_img)
    response = requests.get(url)
    img_bytes = response.content
    st.image(img_bytes, caption=caption_img)
    st.markdown(f'[URL pública al recurso en S3]({url})')

def set_video(subheader_video, url):
    st.subheader(subheader_video)
    response = requests.get(url)
    video_bytes = response.content
    st.video(video_bytes)
    st.markdown(f'[URL pública al recurso en S3]({url})')
