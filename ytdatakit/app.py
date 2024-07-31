import streamlit as st
from ytdatakit.youtube_downloader.app import app as video_downloader
from ytdatakit.youtube_transcript_downloader.app import app as transcript_downloader
from ytdatakit.youtube_thumbnail_downloader.app import app as thumbnail_downloader
from ytdatakit.youtube_channel_downloader.app import app as channel_downloader

import tempfile

app_name = "ytdatakit"
st.set_page_config(page_title=app_name)
st.title(app_name)

tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(["Video downloader", "Transcript downloader", "Thumbnail downloader", "Channel downloader", "💡 About", "Settings"])

with tab4:
    channel_downloader()
with tab1:
    video_downloader()
with tab2:
    transcript_downloader()
with tab3:
    thumbnail_downloader()