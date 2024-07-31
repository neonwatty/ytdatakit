from ytdatakit.youtube_thumbnail_downloader.yt_thumbnail_downloader import get_batch_thumbnails
from ytdatakit.youtube_thumbnail_downloader.zip import zip_images
from ytdatakit.youtube_thumbnail_downloader.state import reset_state
from ytdatakit.youtube_thumbnail_downloader.config import default_thumbnail_location
import streamlit as st
from io import StringIO
import tempfile


def default_temp_savdir():
    with tempfile.TemporaryDirectory() as tmpdirname:
        return tmpdirname


def urls_normalizer(uploaded_file: "st.uploaded", text_urls: str) -> list:
    youtube_urls = []
    if uploaded_file is not None:
        if text_urls is not None:
            if len(text_urls.strip()) > 0:
                st.warning("you can enter urls manually or from file but not both", icon="⚠️")
                st.stop()

        if uploaded_file.type == "text/plain":
            stringio = StringIO(uploaded_file.read().decode("utf-8"))
            for line in stringio:
                youtube_urls.append(line.strip())
    if text_urls is not None:
        if len(text_urls.strip()) > 0:
            if uploaded_file is not None:
                st.warning("you can enter urls manually or from file but not both", icon="⚠️")
                st.stop()
            try:
                text_urls_split = text_urls.split(",")
                text_urls_split = [v.strip() for v in text_urls_split]
                youtube_urls = text_urls_split
            except:  # noqa E722
                st.warning("please check your manually entered urls", icon="⚠️")
                st.stop()
    return youtube_urls


def fetch_logic(youtube_urls: list) -> None:
    if youtube_urls != st.session_state.thumbnail_raw_urls:
        st.session_state.thumbnail_raw_urls = youtube_urls
        reset_state()
    if st.session_state.fetch_count == 0:
        st.session_state.local_thumbnail_location = default_thumbnail_location()
        savedir = "/".join(st.session_state.local_thumbnail_location.split("/")[:-2])
        thumbnail_savepaths, thumbnail_data_entries = get_batch_thumbnails(youtube_urls, savedir)
        st.session_state.thumbnail_savepaths = thumbnail_savepaths
        st.session_state.thumbnail_data_entries = thumbnail_data_entries
        st.session_state.fetch_count += 1

        st.session_state.thumbnails_zip_path = savedir + "/" + "thumbnails.zip"
        zip_images(thumbnail_savepaths)


def fetch_thumbnails(uploaded_file, text_urls):
    # with st.spinner(text="thumbnail pull in progress..."):
    youtube_urls = urls_normalizer(uploaded_file, text_urls)
    fetch_logic(youtube_urls)
