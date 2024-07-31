from ytdatakit.youtube_channel_downloader.callbacks import fetch_channel_videos
from ytdatakit.youtube_channel_downloader.state import state_init, state_reset
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

    video_channel_col_a, video_channel_col_b, video_channel_col_c, video_channel_col_empty = st.columns([4, 3, 2, 2])
    with video_channel_col_a:
        channel_name = st.text_input(
            value=st.session_state.channel_name,
            label="🔗 paste YouTube channel name here",
            placeholder="e.g., littletfitness",
        )
    with video_channel_col_b:
        st.markdown('<p class="custom-font">fetch</p>', unsafe_allow_html=True)
        st.markdown('<span id="button-fetch"></span>', unsafe_allow_html=True)
        fetch_btn = st.button(
            "fetch channel video ids",
            type="primary",
        )
        if fetch_btn:
            if channel_name != st.session_state.channel_name:
                state_reset()
            if st.session_state.channel_fetch_count == 0:
                df_table, df_download = fetch_channel_videos(channel_name)
                st.session_state.channel_data_table = df_table
                st.session_state.channel_data_download = df_download
                st.session_state.channel_fetch_count += 1

    with video_channel_col_c:
        st.markdown('<p class="custom-font">fetch</p>', unsafe_allow_html=True)
        st.markdown('<span id="button-download"></span>', unsafe_allow_html=True)
        st.download_button(
            label="download",
            data=st.session_state.channel_data_download,
            file_name="channel_data.csv",
            mime="text/csv",
            disabled=False if st.session_state.channel_fetch_count > 0 else True,
            type="primary",
        )
    with st.container(border=True):
        st.table(st.session_state.channel_data_table.head(10))
