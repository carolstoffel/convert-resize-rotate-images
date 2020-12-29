#!/usr/bin/python3
from PIL import Image
import os
import shutil
import sys
dir = os.chdir('/home/student-03-33f73cf8f25b/images')
dest = '/opt/icons'
files = os.listdir()
d = '/home/student-03-33f73cf8f25b/images'

for file in files:
    # print('teste')
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
            print(im.size, im.format)
