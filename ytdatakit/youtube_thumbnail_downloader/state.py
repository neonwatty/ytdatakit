import streamlit as st
from ytdatakit.youtube_thumbnail_downloader.config import default_raw_urls, default_thumbnail_savepaths, default_thumbnail_location, default_thumbnail_data_entries


def state_init():
    if "thumbnail_raw_urls" not in st.session_state:
        st.session_state.thumbnail_raw_urls = default_raw_urls
    if "thumbnail_savepaths" not in st.session_state:
        st.session_state.thumbnail_savepaths = default_thumbnail_savepaths
    if "thumbnail_data_entries" not in st.session_state:
        st.session_sate.thumbnail_data_entries = default_thumbnail_data_entries
    if "fetch_count" not in st.session_state:
        st.session_state.fetch_count = 0
    if "default_thumbnail_location" not in st.session_state:
        st.session_state.local_thumbnail_location = default_thumbnail_location()
    if "youtube_thumbnails_expander" not in st.session_state:
        st.session_state.youtube_thumbnails_expander = False


def reset_state():
    if "thumbnail_savepaths" not in st.session_state:
        st.session_state.thumbnail_savepaths = default_thumbnail_savepaths
    if "fetch_count" not in st.session_state:
        st.session_state.fetch_count = 0
    if "youtube_thumbnails_expander" not in st.session_state:
        st.session_state.youtube_thumbnails_expander = False