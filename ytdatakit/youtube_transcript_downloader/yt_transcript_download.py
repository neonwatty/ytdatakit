import re
from typing import List, Dict
from youtube_transcript_api import YouTubeTranscriptApi


def is_valid_youtube_url(url: str) -> bool:
    if not isinstance(url, str):
        return False
    pattern = r"^https://www\.youtube\.com/watch\?v=[A-Za-z0-9_-]{11}$"  # youtube vido ids are always 11 chars long
    if "shorts" in url:
        pattern = r"^https://www\.youtube\.com/shorts/[A-Za-z0-9_-]{11}$"  # youtube vido ids are always 11 chars long
    return re.match(pattern, url) is not None


def get_single_transcript(youtube_url: str) -> dict:
    if is_valid_youtube_url(youtube_url):
        if "shorts" in youtube_url:
            video_id = youtube_url.split("/")[-1]
        else:
            video_id = youtube_url.split("=")[-1]
        try:
            video_transcript = YouTubeTranscriptApi.get_transcript(video_id)
            entry = {}
            entry["youtube_url"] = youtube_url
            entry["video_id"] = video_id
            entry["transcript"] = video_transcript
            return entry
        except Exception as e:
            if "Subtitles are disabled for this video" in str(e):
                entry = {}
                entry["youtube_url"] = youtube_url
                entry["video_id"] = video_id
                entry["transcript"] = "Subtitles are disabled for this video"
                return entry
            else:
                print(e)
    else:
        print(f"FAILURE: youtube_url is not valid - {youtube_url}")


def get_batch_transcripts(youtube_urls: List[str]) -> List[Dict]:
    try:
        entries = []
        for i, youtube_url in enumerate(youtube_urls):
            entry = get_single_transcript(youtube_url)
            if entry is not None:
                entries.append(entry)
        return entries
    except Exception as e:
        print(f"FAILURE: get_batch_transcripts function failed with exception {e}")
        return []
