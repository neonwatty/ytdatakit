from ytdatakit.youtube_downloader.config import video_choices
from ytdatakit.youtube_downloader.callbacks import callback_download_video
from ytdatakit.youtube_downloader.state import state_init
import streamlit as st


def app():
    state_init()
    st.markdown(
        """
    <style>
    .element-container:has(style){
        display: none;
    }
    #button-download {
        display: none;
    }
    .element-container:has(#button-download) {
        display: none;
    }
    .element-container:has(#button-download) + div button {
        background-color: green;
        border-color: green;
        }
    #button-fetch {
        display: none;
    }
    .element-container:has(#button-fetch) {
        display: none;
    }
    .element-container:has(#button-fetch) + div button {
        background-color: blue;
        border-color: blue;
        }
    </style>
    """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
    <style>
    .custom-font {
        font-size:7.5px !important;
        color: transparent;
    }
    </style>
    """,
        unsafe_allow_html=True,
    )

    video_download_col_a, video_download_col_b, video_download_col_c = st.columns([4, 3, 2])
    with video_download_col_a:
        url_input = st.text_input(
            value="https://www.youtube.com/shorts/43BhDHYBG0o",
            label="🔗 Paste YouTube / Shorts URL here",
            placeholder="e.g., https://www.youtube.com/watch?v=.",
            key="youtube_download_text_input"
        )
    with video_download_col_b:
        resolution_dropdown = st.selectbox(options=video_choices, index=st.session_state.youtube_download_resolution_index, label="video resolution")
    with video_download_col_c:
        st.markdown('<p class="custom-font">fetch</p>', unsafe_allow_html=True)
        st.markdown('<span id="button-fetch"></span>', unsafe_allow_html=True)
        st.button(
            "fetch video",
            type="primary",
            on_click=callback_download_video,
            args=(
                url_input,
                resolution_dropdown,
            ),
            key="youtube_download_fetch_button"
        )
    with st.container(border=True):
        with open(st.session_state.youtube_download_location, "rb") as file:
            st.markdown('<span id="button-download"></span>', unsafe_allow_html=True)
            st.download_button(
                label="download video",
                data=file,
                file_name=st.session_state.youtube_download_location.split("/")[-1],
                mime="video/mp4",
                type="primary",
            )
        st.video(data=st.session_state.youtube_download_location, format="video/mp4")
