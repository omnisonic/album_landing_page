from jinja2 import Environment, FileSystemLoader
import os

#### jinja  this inserts paths for the audio into the player.js


file_loader = FileSystemLoader('templates')
env = Environment(loader=file_loader)

path = 'waterfront_album_1pg/static/audio/waterfront-preview'
files = os.listdir(path)
files.sort()
print(files)

##### jinja added by jhc

# title = [t.data['title'] for t in album.tracks]
title = files
template = env.get_template('player.js')

output = template.render(title=title, path=path)
# print(output)

f = open("demofile2.txt", "w")
f.write(output)
f.close()