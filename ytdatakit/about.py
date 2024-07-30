import streamlit as st


def about():
    return st.markdown(
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
