import os
import moviepy.editor

if not os.path.isdir("mp3"):
    os.mkdir("mp3")
for VideoName in os.listdir():
    if VideoName.endswith(".mp4"):
        video=moviepy.editor.VideoFileClip(VideoName)
        audio=video.audio
        VideoName=VideoName.strip(".mp4")
        audio.write_audiofile(f"mp3/{VideoName}.mp3")
        print(f"\033[36;1m {VideoName} Ready \033[36;0m")
print(f"\033[32;1m Done .. . . . . . . . . . . .  ! ")


