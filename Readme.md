# Youtube Audio Downloader

Simple python CLI youtube audio downloader.

## How to use?

Start programme with:

```powershell
python single_audio_dl.py
```

Programme output:

```powershell
Please provide a valid youtube link:
https://www.youtube.com/watch?v=video_id

Loading available audio tracks (this may take a few seconds):
1: <Stream: itag="139" mime_type="audio/mp4" abr="48kbps" acodec="mp4a.40.5" progressive="False" type="audio">
2: <Stream: itag="140" mime_type="audio/mp4" abr="128kbps" acodec="mp4a.40.2" progressive="False" type="audio">
3: <Stream: itag="249" mime_type="audio/webm" abr="50kbps" acodec="opus" progressive="False" type="audio">
4: <Stream: itag="250" mime_type="audio/webm" abr="70kbps" acodec="opus" progressive="False" type="audio">

Choose an option (number):
2
You chose option 1
Will start downloading:
<Stream: itag="140" mime_type="audio/mp4" abr="128kbps" acodec="mp4a.40.2" progressive="False" type="audio">

Downloaded file to:
C:\path\to\file\...\audio_ytdl\video_track_name.mp4
```
