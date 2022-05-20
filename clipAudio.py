# from ffmpeg_tools import ffmpeg_extract_subclip

# ffmpeg_extract_subclip("static/audio/john-h-clarke/mosaic-for-shadows/10 - mosaic-for-shadows.mp3", 0, 10, targetname="result/shorter_audio.mp3")


#needed it pipenv install ffmpeg-python

import ffmpeg  
import os

path = '/Users/omnisonic/Downloads/John H. Clarke - Acoustik Guitar - Full Album'
files = os.listdir(path)

for f in files:
    if f.endswith('mp3'):
        
        audio_input = ffmpeg.input(f'/Users/omnisonic/Downloads/John H. Clarke - Acoustik Guitar - Full Album/{f}')
        audio_cut = audio_input.audio.filter('atrim', duration=30)
        audio_output = ffmpeg.output(audio_cut, f'/Users/omnisonic/Documents/code/MyWebDev/album_landing_page/static/audio/john-h-clarke/acoustik-guitar-preview/{f}')
        ffmpeg.run(audio_output)