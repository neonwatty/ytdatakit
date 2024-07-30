import streamlit as st
import tempfile


def default_youtube_download_location():
    with tempfile.TemporaryDirectory() as tmpdirname:
        return tmpdirname


def state_init():
    if "thumbnail_raw_urls" not in st.session_state:
        st.session_state.thumbnail_raw_urls = []
    if "thumbnail_savepaths" not in st.session_state:
        st.session_state.thumbnail_savepaths = []
    if "thumbnails_zip_path" not in st.session_state:
        st.session_state.thumbnails_zip_path = default_youtube_download_location() + "/" + "thumbnails.zip"
