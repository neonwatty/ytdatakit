import io
import tempfile
from youtube_downloader.yt_download import download_video
import streamlit as st

video_choices = ["best", "1080", "720", "360"]


app_name = "ytdatakit"
st.set_page_config(page_title=app_name)
st.title(app_name)


def download_this(url_input, resolution_dropdown):
    temporary_video_location = download_video(url_input, tmpdirname, resolution_dropdown)

    filename = open(temporary_video_location, "rb")
    byte_file = io.BytesIO(filename.read())
    with open(temporary_video_location, "wb") as out:
        out.write(byte_file.read())

    new_og_video = gr.Video(
        value=temporary_video_location,
        visible=True,
        show_download_button=True,
        show_label=True,
        label="your video",
        format="mp4",
        width="50vw",
        height="50vw",
    )

    return new_og_video


with tempfile.TemporaryDirectory() as tmpdirname:
    video_download_col_a, video_download_col_b, video_download_col_c = st.columns([4, 3, 2])
    with video_download_col_a:
        url_input = st.text_input(
            value="https://www.youtube.com/shorts/43BhDHYBG0o",
            label="🔗 Paste YouTube / Shorts URL here",
            placeholder="e.g., https://www.youtube.com/watch?v=.",
            max_lines=1,
        )
    with video_download_col_b:
        resolution_dropdown = st.selectbox(
            options=video_choices, index=0, label="video resolution"
        )
    with video_download_col_c:
        download_button = st.button("download", type="primary")

    with st.container(border=True):
        og_video = st.video(
            label="your video",
            use_column_width="always"
        )




with gr.TabItem("💡 About"):
with gr.Blocks() as about:
    gr.Markdown(
        (
            "### About \n"
            "Some notes on how this works: \n\n"
            "1.  **youtube / google login**: you do **not** need to be logged into a google account to use the app, with one exception: age restricted videos"
            "2.  **age restricted videos**: this app cannot fetch age restricted videos yet, which requires a user login to google / youtube - this feature is not yet available"
            "3.  **video resolution**: not all videos have all possible resolutions, so you may not be able to fetch the resolution you want for some videos (as they don't exist) \n"
            "4.  **recommended hardware**: this is a very light weight app, so minimum specs should work fine"
            "5.  **proxies**: there is an option in the yt_download module to enter proxy server ips"
        )
    )
