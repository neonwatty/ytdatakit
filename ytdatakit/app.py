import streamlit as st
from ytdatakit.youtube_downloader.app import app as video_downloader
from ytdatakit.youtube_transcript_downloader.app import app as transcript_downloader
from ytdatakit.youtube_thumbnail_downloader.app import app as thumbnail_downloader


app_name = "ytdatakit"
st.set_page_config(page_title=app_name)
st.title(app_name)

tab1, tab2, tab3, tab4, tab5 = st.tabs(["Video downloader", "Transcript downloader", "Thumbnail downloader", "💡 About", "Settings"])

with tab1:
    thumbnail_downloader()
with tab2:
    video_downloader()
with tab3:
    transcript_downloader()
