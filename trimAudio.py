#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Author: Yedarm Seong
Python Version: 3.6.1
"""

# python3 -m pip install pydub
import os
from pydub import AudioSegment

def audio_crop(start, end, old_file, new_file, fmt='mp3'):
    try:
        wav_file = AudioSegment.from_file(old_file)
        crop_file = wav_file[start:end]
        crop_file.export(new_file, format=fmt)
        print('success! ' + old_file)
    except Exception as e:
        print('error! ' + old_file)

# start, end is ms unit
path = './static/audio/john-h-clarke/acoustik-guitar-full-album'
files = os.listdir(path)
files.sort()
print(files)

for file in files:
    audio_crop(0, 1000, file, f'"short"{file}')