import streamlit as st
from ytdatakit.youtube_downloader.yt_download import download_video
from ytdatakit.youtube_downloader.state import default_youtube_download_location
from ytdatakit.youtube_downloader.config import video_choices


def callback_download_video(url_input: str, resolution_dropdown: str) -> None:
    temporary_video_location = download_video(url_input, default_youtube_download_location(), st.session_state.resolution_dropdown)
    st.session_state.youtube_download_location = temporary_video_location
    st.session_state.youtube_download_resolution_index = video_choices.index(resolution_dropdown)
