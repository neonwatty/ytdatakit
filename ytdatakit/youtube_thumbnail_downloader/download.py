import requests


def download_thumbnail(yt_thumbnail_url: str, yt_title: str, save_dir: str) -> str:
    img_data = requests.get(yt_thumbnail_url).content
    img_ext = yt_thumbnail_url.split(".")[-1]
    savepath = save_dir + "/" + yt_title + "." + img_ext
    with open(savepath, "wb") as handler:
        handler.write(img_data)
    return savepath