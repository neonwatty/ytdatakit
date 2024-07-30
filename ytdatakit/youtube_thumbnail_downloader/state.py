import streamlit as st


def state_init():
    if "thumbnail_raw_urls" not in st.session_state:
        st.session_state.thumbnail_raw_urls = ""
    if "thumbnail_savepaths" not in st.session_state:
        st.session_state.thumbnail_savepaths = []
