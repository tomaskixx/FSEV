from pytubefix import YouTube
from pytubefix.cli import on_progress

url = input("Enter video URL: ")
yt = YouTube(url, on_progress_callback=on_progress)


def get_audio_itag():
    max_audio = 0
    audio_value = 0

    # Find the best audio stream
    for audio_stream in yt.streams.filter(only_audio=True):
        if audio_stream.abr:
            abr = int(audio_stream.abr.replace('kbps', ''))
            if abr > max_audio:
                max_audio = abr
                audio_value = audio_stream.itag

    if not audio_value:
        raise ValueError("No suitable audio stream found.")
    
    return audio_value


# Main logic
try:
    audio_itag = get_audio_itag()
    print(f"Audio itag: {audio_itag}")

    # Download audio stream
    audio_stream = yt.streams.get_by_itag(audio_itag)
    if audio_stream:
        audio_stream.download()
        print("Audio downloaded successfully.")
    else:
        print("No audio stream found for the selected itag.")

except ValueError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
