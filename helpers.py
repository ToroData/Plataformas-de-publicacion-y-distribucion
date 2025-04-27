import streamlit as st

def set_img(img_path, caption_img, subheader_img=None):
    if subheader_img:
        st.subheader(subheader_img)
    st.image(img_path, caption=caption_img)

def set_video(subheader_video, video_path):
    st.subheader(subheader_video)
    st.video(video_path)
