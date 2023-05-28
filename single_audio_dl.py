from pytube import YouTube
import os
import sys
import random

# url input from user
print("Please provide a valid youtube link:")
yt_link = input()
yt_link = yt_link.strip()

yt = None

try:
    yt = YouTube(url=yt_link)
    print()
except:
    print("Invalid YouTube link provided.")
    print("Exiting...")
    sys.exit(random.randint(-1_000_000, -1))

print("Loading available audio tracks (this may take a few seconds):")
# extract only audio
audio_tracks = yt.streams.filter(only_audio=True)

# Print available tracks to download.
for index, track in zip(range(1, len(audio_tracks)), audio_tracks):
    print(f"{index}: {track}")

print()
print("Choose an option (number):")
option = input()

trackIndex = 0

try:
    trackIndex = int(option)

except ValueError:
    print("Incorrect input provided.")
    print("Exiting...")
    sys.exit(random.randint(-1_000_000, -1))

# Verify input is withing available options.
if trackIndex < 0 or trackIndex > len(audio_tracks):
    print("Incorrect option given.")
    print("Exiting...")
    sys.exit(random.randint(-1_000_000, -1))


chosen_track = audio_tracks[trackIndex]
print(f"You chose option {trackIndex}")
print("Will start downloading:")
print(chosen_track)
print()

# Download audio track.
try:
    output_file = chosen_track.download(os.getcwd())

    print("Downloaded file to:", output_file)
except:
    print("Error: Failed to download audio track.")
