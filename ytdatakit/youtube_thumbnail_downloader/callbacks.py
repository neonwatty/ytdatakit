from ytdatakit.youtube_thumbnail_downloader.yt_thumbnail_downloader import get_batch_thumbnails
from ytdatakit.youtube_thumbnail_downloader.zip import zip_images
from io import StringIO
import pandas as pd
import streamlit as st


def fetch_thumbnails(uploaded_file, text_urls):
    with st.spinner(text="thumbnail pull in progress..."):
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
        
        thumbnail_savepaths, data_entries = get_batch_thumbnails(youtube_urls)
        zip_images(thumbnail_savepaths, st.session_data.thumbnails_zip_path)
        return thumbnail_savepaths, data_entries

