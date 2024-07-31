import streamlit as st
from ytdatakit.youtube_thumbnail_downloader.state import state_init
from ytdatakit.youtube_thumbnail_downloader.callbacks import fetch_thumbnails


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
            value=st.session_state.thumbnail_text_input_urls if "thumbnail_text_input_urls" in st.session_state else "",
            placeholder="https://www.youtube.com/shorts/o7a9hx-Pqyo, https://www.youtube.com/shorts/xkAYLnIsfX4, ....",
            key="thumbnail_urls_input",
        )
        st.thumbnail_text_input_urls = text_urls
        uploaded_file = st.file_uploader("Choose a File", type=["txt"], key="thumbanils_file_uploader")
        thumbnail_col_1, thumbnail_col_2, thumbnail_col_3 = st.columns([5, 8, 8])
        with thumbnail_col_1:
            st.markdown('<span id="button-fetch"></span>', unsafe_allow_html=True)
            st.button(label="fetch thumbnails", type="primary", on_click=fetch_thumbnails, args=(uploaded_file, text_urls))

        with thumbnail_col_2:
            st.markdown('<span id="button-download"></span>', unsafe_allow_html=True)
            if "thumbnails_zip_path" in st.session_state:
                with open(st.session_state.thumbnails_zip_path, "rb") as file:
                    st.download_button(
                        label="download thumbnails",
                        data=file, #st.session_state.thumbnails_zip_path if "thumbnails_zip_path" in st.session_state else "./data/input/blank.zip",
                        file_name="thumbnails.zip",
                        mime="application/zip",
                        type="primary",
                        disabled=True if st.session_state.fetch_count == 0 else False
                        )
            else:
                st.download_button(
                    label="download thumbnails",
                    data="./data/input/blank.zip",
                    file_name="thumbnails.zip",
                    mime="application/zip",
                    type="primary",
                    disabled=True
                    )

        with st.container(border=True):
            for ind, thumbnail_savepath in enumerate(st.session_state.thumbnail_savepaths):
                title = st.session_state.thumbnail_data_entries[ind]["video_title"]
                thumbnail_savepath = st.session_state.thumbnail_savepaths[ind]
                with st.container(border=True):
                    a, b, c = st.columns([1, 3, 1])
                    with b:
                        st.subheader(title)
                        st.image(thumbnail_savepath)
                        with open(thumbnail_savepath, "rb") as file:
                            st.download_button(
                                label="download thumbnail",
                                data=file,
                                file_name=title + ".jpg",
                                mime="image/jpg",
                                key=f"{title} download",
                                type="primary",
                            )
