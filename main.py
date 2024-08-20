import moviepy.editor as mp

my_clip = mp.VideoFileClip(r"1.mp4")
my_clip.audio.write_audiofile(r"1.mp3")
