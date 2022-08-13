from jinja2 import Environment, FileSystemLoader
import os
import sys


sys.path.append('trio_album_1pg')
import config

# an album link source is: https://odesli.co/


js_output = f'./{config.project_dir}/static'
audio_files = 'static/audio'


#Variables for index template
Title = config.Title
Apple = config.Apple
Amazon = config.Amazon
Pandora = config.Pandora
YouTubeMusic = config.YouTubeMusic
Spotify = config.Spotify
Bandcamp = config.Bandcamp
Tidal = config.Tidal

#### jinja  this inserts paths for the audio into the player.js

file_loader = FileSystemLoader('templates')
env = Environment(loader=file_loader)

path = audio_files  

file_names = os.listdir(f'{config.project_dir}/{path}')
file_names.remove('.DS_Store')

        
file_names.sort()
print(file_names)

##### jinja added by jhc

# title = [t.data['title'] for t in album.tracks]
title = file_names # list object of audio track filenames
template = env.get_template('player.js')

output = template.render(title=title, path=path) # using .strip() to remove from filename
# print(output)

f = open(f"{js_output}/player.js", "w")
f.write(output)
f.close()

## jinja for index template

file_loader = FileSystemLoader('templates')
env = Environment(loader=file_loader)


template = env.get_template('index.html')
output = template.render(Title=Title, Apple=Apple, Amazon=Amazon, Panora=Pandora, Bandcamp=Bandcamp, YouTubeMusic=YouTubeMusic, Spotify=Spotify)

f = open(f"{config.html_output}/index.html", "w")
f.write(output)
f.close()