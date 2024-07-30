import streamlit as st
import pandas as pd


def state_init():
    df = pd.DataFrame(columns=["youtube_url", "video_id", "transcript"])
    if "transcript_raw_urls" not in st.session_state:
        st.session_state.transcript_raw_urls = ""
    if "transcript_data_table" not in st.session_state:
        st.session_state.transcript_data_table = df
    if "transcript_data_download" not in st.session_state:
        st.session_state.transcript_data_download = df.to_csv().encode("utf-8")