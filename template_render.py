from jinja2 import Environment, FileSystemLoader
import os

# an album link source is: https://odesli.co/

# input and output variables
project_dir = './string_and_wood_album_1pg'

html_output = './string_and_wood_album_1pg'
js_output = f'./{project_dir}/static'
audio_files = 'static/audio'


#Variables for index template
Title = 'String and Wood - By John H. Clarke'
Apple = 'https://geo.music.apple.com/us/album/_/455063415'
Amazon = 'https://amazon.com/dp/B0019GLCD8'
Pandora = 'https://www.pandora.com/AL:15147199'
YouTubeMusic = 'https://music.youtube.com/playlist?list=OLAK5uy_kUvjXmAWYXp8acz1v8NA19egUnUUSWlzk'
Bandcamp = 'https://johnhclarke.bandcamp.com/album/string-wood-full-album'
Spotify = 'https://open.spotify.com/album/2Wx6nK8uk3B8wQOGIollBv'

#### jinja  this inserts paths for the audio into the player.js

file_loader = FileSystemLoader('templates')
env = Environment(loader=file_loader)

path = audio_files  

file_names = os.listdir(f'{project_dir}/{path}')
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

f = open(f"{html_output}/index.html", "w")
f.write(output)
f.close()