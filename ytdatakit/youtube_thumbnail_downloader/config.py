import tempfile
import uuid

default_thumbnail_raw_urls = ""
default_thumbnail_savepaths = []
default_thumbnail_data_entries = []
default_thumbnail_text_input_urls = ""
default_thumbnails_zip_path = "./data/input/blank.zip"


def default_thumbnail_location():
    with tempfile.TemporaryDirectory() as tmpdirname:
        return tmpdirname + "/temp_" + str(uuid.uuid4()) + ".jpg"
