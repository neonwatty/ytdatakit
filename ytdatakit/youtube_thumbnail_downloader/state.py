import streamlit as st
from ytdatakit.youtube_thumbnail_downloader.config import (
    default_thumbnail_raw_urls,
    default_thumbnail_savepaths,
    default_thumbnail_location,
    default_thumbnail_data_entries,
    default_thumbnail_text_input_urls,
    default_thumbnails_zip_path,
)


def state_init():
    if "thumbnail_raw_urls" not in st.session_state:
        st.session_state.thumbnail_raw_urls = default_thumbnail_raw_urls
    if "thumbnail_savepaths" not in st.session_state:
        st.session_state.thumbnail_savepaths = default_thumbnail_savepaths
    if "thumbnail_data_entries" not in st.session_state:
        st.session_state.thumbnail_data_entries = default_thumbnail_data_entries
    if "fetch_count" not in st.session_state:
        st.session_state.fetch_count = 0
    if "default_thumbnail_location" not in st.session_state:
        st.session_state.local_thumbnail_location = default_thumbnail_location()
    if "youtube_thumbnails_expander" not in st.session_state:
        st.session_state.youtube_thumbnails_expander = False


def reset_state():
    st.session_state.thumbnail_savepaths = default_thumbnail_savepaths
    st.session_state.thumbnail_text_input_urls = default_thumbnail_text_input_urls
    st.session_state.thumbnails_zip_path = default_thumbnails_zip_path
    st.session_state.thumbnail_text_input_urls = ""

    st.session_state.fetch_count = 0
    st.session_state.youtube_thumbnails_expander = False
