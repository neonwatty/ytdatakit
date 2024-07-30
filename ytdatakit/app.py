import streamlit as st
from youtube_downloader.app import video_downloader


app_name = "ytdatakit"
st.set_page_config(page_title=app_name)
st.title(app_name)

tab1, tab2, tab3, tab4, tab5 = st.tabs(["Video downloader", "Transcript downloader", "Thumbnail downloader", "💡 About", "Settings"])


with tab1:
    video_downloader()