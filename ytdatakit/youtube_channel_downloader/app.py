from ytdatakit.youtube_channel_downloader.callbacks import fetch_channel_videos
from ytdatakit.youtube_channel_downloader.state import state_init
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

    video_channel_col_a, video_channel_col_b, video_channel_col_c = st.columns([4, 3, 2])
    with video_channel_col_a:
        channel_name = st.text_input(
            value="",
            label="🔗 paste YouTube channel name here",
            placeholder="e.g., littletfitness",
        )
    with video_channel_col_b:
        st.markdown('<p class="custom-font">fetch</p>', unsafe_allow_html=True)
        st.markdown('<span id="button-fetch"></span>', unsafe_allow_html=True)
        st.button(
            "fetch channel video ids",
            type="primary",
            on_click=fetch_channel_videos,
            args=(
                channel_name,
            ),
        )
    with st.container(border=True):
        st.table(st.session_state.channel_data_table)