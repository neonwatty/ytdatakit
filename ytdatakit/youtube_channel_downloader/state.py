import streamlit as st
import pandas as pd
from ytdatakit.youtube_channel_downloader.config import default_channel_name


def state_init():
    df = pd.DataFrame(columns=["youtube_url", "video_id"])
    if "channel_data_table" not in st.session_state:
        st.session_state.channel_data_table = df
    if "channel_data_download" not in st.session_state:
        st.session_state.channel_data_download = df.to_csv().encode("utf-8")
    if "channel_name" not in st.session_state:
        st.session_state.channel_name = default_channel_name
    if "channel_fetch_count" not in st.session_state:
        st.session_state.channel_fetch_count = 0


def state_reset():
    df = pd.DataFrame(columns=["youtube_url", "video_id"])
    if "channel_data_table" not in st.session_state:
        st.session_state.channel_data_table = df
    if "channel_data_download" not in st.session_state:
        st.session_state.channel_data_download = df.to_csv().encode("utf-8")
    st.session_state.channel_fetch_count = 0
