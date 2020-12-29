#!/usr/bin/python3
from PIL import Image
import os
import shutil
import sys
dir = os.chdir('DIGITE A PASTA DE ORIGEM')
dest = 'DIGITE A PASTA DE DESINO'
files = os.listdir()
for file in files:
    try:
        file, extension = os.path.splitext(file)
        out = file + '.jpeg'
    except:
        pass
    if file[0] == ".":
        continue
    if file != out:
        with Image.open(file) as im:
            im = im.rotate(270).resize((128, 128)).convert("RGB")
            im.save(os.path.join(dest, out))

