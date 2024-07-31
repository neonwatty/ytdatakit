from ytdatakit.youtube_channel_downloader.yt_channel_download import get_channel_videos
import pandas as pd
import streamlit as st
import copy


@st.cache_data
def convert_df(df: pd.DataFrame) -> "csv":
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
    return df.to_csv().encode("utf-8")


def fetch_channel_videos(channel_name: str):
    with st.spinner(text="channel video ids pull in progress..."):
        video_ids, video_urls = get_channel_videos(channel_name)
        df_table = pd.DataFrame([video_ids, video_urls])
        df_download = convert_df(df_table)
        return df_table, df_download
