import streamlit as st
from ytdatakit.youtube_thumbnail_downloader.config import default_raw_urls, default_thumbnail_savepaths


def state_init():
    if "thumbnail_raw_urls" not in st.session_state:
        st.session_state.thumbnail_raw_urls = default_raw_urls
    if "thumbnail_savepaths" not in st.session_state:
        st.session_state.thumbnail_savepaths = default_thumbnail_savepaths
    if "fetch_count" not in st.session_state:
        st.session_state.fetch_count = 0
    if "transcribe_count" not in st.session_state:
        st.session_state.transcribe_count = 0
    if "gif_expander" not in st.session_state:
        st.session_state.gif_expander = False