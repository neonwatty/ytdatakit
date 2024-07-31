import yt_dlp
import scrapetube
from typing import Tuple


def get_channel_id_from_name(channel_name: str) -> str | None:
    ydl_opts = {
        'quiet': True,
        'skip_download': True,
        'extract_flat': True,
        'force_generic_extractor': True,
    }
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            info = ydl.extract_info(f'ytsearch1:{channel_name}', download=False)
            return info["entries"][0]["channel_id"]
        except Exception as e:
            print(f"FAILURE: get_channel_id_from_name failed with exception {e}")
            return None


def get_videourl_from_channel_id(channel_id: str) -> Tuple[list, list] | Tuple[None, None]:
    try:
        videos = scrapetube.get_channel(channel_id)
        video_urls = []
        video_ids = []
        for video in videos:
            vid = video['videoId']
            vurl = "https://www.youtube.com/watch?v=" + vid
            video_ids.append(vid)
            video_urls.append(vurl)
        return video_ids, video_urls
    except Exception as e:
        print(f"FAILURE: get_videourls_from_channel_id failed with exception {e}")
        return None, None


def get_channel_videos(channel_name: str) -> Tuple[list, list] | Tuple[None, None]:
    try:
        print("INFO: starting channel video id puller...")
        channel_id = get_channel_id_from_name(channel_name)
        if channel_id is not None:
            video_ids, video_urls = get_videourl_from_channel_id(channel_id)
            if video_ids is not None and video_urls is not None:
                print("...done!")
                return video_ids, video_urls
            else:
                print("...done!")
                return None, None
        else:
            print("...done!")
            return None, None
    except Exception as e:
        print(f"FAILURE: get_channel_videos failed with exception {e}")
        return None, None
