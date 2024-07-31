import zipfile
import os
import streamlit as st


def zip_images(image_paths: list):
    print("INFO: zipping images...")
    zip_filename = st.session_state.thumbnails_zip_path
    with zipfile.ZipFile(zip_filename, "w") as zipf:
        for image_path in image_paths:
            _, filename = os.path.split(image_path)
            zipf.write(image_path, arcname=filename)
            print(f"Added {filename} to the zip file.")
    print(f"...done!  images have been zipped into {zip_filename}")
