from ytdatakit.youtube_transcript_downloader.callbacks import fetch_transcripts
from ytdatakit.youtube_transcript_downloader.state import state_init
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

    base = st.container(border=True)
    with base:
        text_urls = st.text_area(
            "youtube urls separated by commas",
            value=st.session_state.transcript_raw_urls,
            placeholder="https://www.youtube.com/shorts/o7a9hx-Pqyo, https://www.youtube.com/shorts/xkAYLnIsfX4, ....",
            key="transcript_urls_input"
        )
        uploaded_file = st.file_uploader("Choose a File", type=["txt"], key="transcripts_file_uploader")
        transcript_col_1, transcript_col_2, transcript_col_3 = st.columns([3, 4, 6])
        with transcript_col_1:
            st.markdown('<span id="button-fetch"></span>', unsafe_allow_html=True)
            fetch_btn = st.button(
                label="fetch transcripts",
                type="primary",
            )
            if fetch_btn:
                df_table, df_download = fetch_transcripts(uploaded_file, text_urls)
                st.session_state.transcript_data_table = df_table
                st.session_state.transcript_data_download = df_download
        with transcript_col_2:
            st.markdown('<span id="button-download"></span>', unsafe_allow_html=True)
            st.download_button(
                label="download transcripts",
                data=st.session_state.transcript_data_download,
                file_name="transcripts.csv",
                mime="text/csv",
                disabled=False,
                type="primary",
            )
        with st.container(border=True):
            st.table(st.session_state.transcript_data_table)
