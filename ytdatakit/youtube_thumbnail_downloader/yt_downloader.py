import re
import requests
import yt_dlp
from yt_dlp import YoutubeDL


def is_valid_youtube_url(url: str) -> bool:
    if not isinstance(url, str):
        return False
    pattern = r"^https://www\.youtube\.com/watch\?v=[A-Za-z0-9_-]{11}$"  # youtube vido ids are always 11 chars long
    if "shorts" in url:
        pattern = r"^https://www\.youtube\.com/shorts/[A-Za-z0-9_-]{11}$"  # youtube vido ids are always 11 chars long
    return re.match(pattern, url) is not None


def download_thumbnail(yt_thumbnail_url: str, savepath: str) -> None:
    img_data = requests.get(yt_thumbnail_url).content
    with open(savepath, "wb") as handler:
        handler.write(img_data)


def get_youtube_thumbnail_url(video_id: str) -> dict:
    if video_id:
        return {
            'default': f'https://img.youtube.com/vi/{video_id}/default.jpg',
            'mqdefault': f'https://img.youtube.com/vi/{video_id}/mqdefault.jpg',
            'hqdefault': f'https://img.youtube.com/vi/{video_id}/hqdefault.jpg',
            'sddefault': f'https://img.youtube.com/vi/{video_id}/sddefault.jpg',
            'maxresdefault': f'https://img.youtube.com/vi/{video_id}/maxresdefault.jpg'
        }


def pull_yt_data(url: str, savedir: str, my_proxies: dict = {}) -> str:
    try:
        if is_valid_youtube_url(url):
            with YoutubeDL() as ydl:
                info_dict = ydl.extract_info(url, download=False)
                video_url = info_dict.get("url", None)
                video_id = info_dict.get("id", None)
                video_title = info_dict.get("title", None)
                if video_title is None:
                    savepath = savedir + "/" + video_id + ".jpg"
                else:
                    savepath = savedir + "/" + video_title + ".jpg"
                    
                if video_id:
                    thumbnail_url = get_youtube_thumbnail_url(video_id)["sddefault"]
                    download_thumbnail(thumbnail_url, savepath)

            print("...done!")
            return savepath
        else:
            raise ValueError(f"invalid input url: {url}")
    except Exception as e:
        raise ValueError(f"yt_download failed with exception {e}")


def get_yt_thumbnails(yt_urls: list, savedir: str, my_proxies: dict = {}):
    try:
        savepaths = []
        for url in yt_urls:
            savepath = pull_yt_data(url, savedir, my_proxies)
            savepaths.append(savepath)
    except:
        pass