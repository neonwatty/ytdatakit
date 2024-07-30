from ytdatakit.youtube_transcript_downloader.yt_transcript_download import get_batch_transcripts
from io import StringIO
import pandas as pd
import streamlit as st
import copy


@st.cache_data
def convert_df(df: pd.DataFrame) -> "csv":
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
    return df.to_csv().encode("utf-8")


def fetch_transcripts(uploaded_file, text_urls):
    with st.spinner(text="transcript pull in progress..."):
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
        
        batch_transcripts = get_batch_transcripts(youtube_urls)
        df = pd.DataFrame(batch_transcripts)
        df_download = convert_df(df)
        
        def truncate_and_append(text, length, suffix):
            if len(text) > length:
                return text[:length] + suffix
            return text
        max_length = 100
        suffix = '...'
        df_table = copy.deepcopy(df).astype(str)
        df_table['transcript'] = df_table['transcript'].apply(lambda x: truncate_and_append(x, max_length, suffix))
        return df_table, df_download

