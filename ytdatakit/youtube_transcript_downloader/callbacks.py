import pandas as pd
from ytdatakit.youtube_transcript_downloader.yt_transcript_download import get_batch_transcripts


@st.cache_data
def convert_df(df: pd.DataFrame) -> "csv":
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
    return df.to_csv().encode("utf-8")


def button_logic(youtube_short_urls: list) -> None:
    if trans_button_val:
        batch_transcripts = get_batch_transcripts(youtube_short_urls)
        df = pd.DataFrame(batch_transcripts)
        converted_dv = convert_df(df)
        st.write(df.head(1).to_dict())

        with download_area:
            st.download_button(
                label="Download transcripts",
                data=converted_dv,
                file_name="output.csv",
                mime="text/csv",
                disabled=False,
                type="primary",
            )