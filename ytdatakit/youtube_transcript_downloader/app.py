from ytdatakit.youtube_transcript_downloader.callbacks import fetch_transcripts
import streamlit as st


def app():
    base = st.container(border=True)
    with base:
        col1, col2, col3 = st.columns([5, 5, 3])
        with col1:
            text_urls = st.text_area(
                "youtube urls separated by commas",
                value=st.session_state.transcript_raw_urls,
                placeholder="https://www.youtube.com/shorts/o7a9hx-Pqyo, https://www.youtube.com/shorts/xkAYLnIsfX4, ....",
            )
        with col2:
            uploaded_file = st.file_uploader("Choose a File", type=["txt"])
        with col3:
            st.download_button(
                label="Download transcripts",
                data=st.session_state.transcript_data,
                file_name="output.csv",
                mime="text/csv",
                disabled=False,
                type="primary",
                on_click=fetch_transcripts,
                args=(uploaded_file, text_urls, )
            )
