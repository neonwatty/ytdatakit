import streamlit as st


def state_init():
    if "transcript_raw_urls" not in st.session_state:
        st.session_state.transcript_raw_urls = ""
    if "transcript_data" not in st.session_state:
        st.session_state.transcript_data = None