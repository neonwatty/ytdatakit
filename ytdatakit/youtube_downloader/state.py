from ytdatakit.youtube_downloader.config import video_choices, default_clip_video_path
import streamlit as st
import tempfile


def default_youtube_download_location():
    with tempfile.TemporaryDirectory() as tmpdirname:
        return tmpdirname


def state_init():
    if "resolution_dropdown" not in st.session_state:
        st.session_state.resolution_dropdown = video_choices
    if "youtube_download_location" not in st.session_state:
        st.session_state.youtube_download_location = default_clip_video_path
    if "youtube_download_resolution_index" not in st.session_state:
        st.session_state.youtube_download_resolution_index = 0
