from ytdatakit.youtube_downloader.config import app_name, video_choices
from ytdatakit.youtube_downloader.callbacks import callback_download_video
from ytdatakit.youtube_downloader.state import state_init
import streamlit as st

state_init()


def app():
    video_download_col_a, video_download_col_b, video_download_col_c = st.columns([4, 3, 2])
    with video_download_col_a:
        url_input = st.text_input(
            value="https://www.youtube.com/shorts/43BhDHYBG0o",
            label="🔗 Paste YouTube / Shorts URL here",
            placeholder="e.g., https://www.youtube.com/watch?v=.",
        )
    with video_download_col_b:
        resolution_dropdown = st.selectbox(options=video_choices, index=st.session_state.youtube_download_resolution_index, label="video resolution")
    with video_download_col_c:
        st.button("download", type="primary", on_click=callback_download_video, args=(url_input, resolution_dropdown, ))
    with st.container(border=True):
        st.video(data=st.session_state.youtube_download_location, format="video/mp4")
