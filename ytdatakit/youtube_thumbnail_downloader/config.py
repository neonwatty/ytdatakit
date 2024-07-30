import tempfile


default_thumbnail_raw_urls = ""
default_thumbnail_savepaths = []
default_thumbnail_data_entries = []


def default_thumbnail_location():
    with tempfile.TemporaryDirectory() as tmpdirname:
        return tmpdirname + "/original_" + str(uuid.uuid4()) + ".mp4"