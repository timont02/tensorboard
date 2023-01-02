import os
from os import listdir
from PIL import Image, ImageOps
from pathlib import Path


images_path = (r"C:\Users\Timon\Documents\Studium\Semester 5\ML\resize\T4")
resized_images_path = images_path + '_resized'
os.mkdir(resized_images_path)
new_height = 720
i = 1
for images in os.listdir(images_path):
    im = Image.open(os.path.join(images_path, images))
    im = ImageOps.exif_transpose(im)
    new_width = int(new_height/im.height*im.width)
    resized_img = im.resize((new_width, new_height))
    resized_img.save(os.path.join(resized_images_path, 'tomato_' + str(i) + '.jpg'))
    i = i+1
    



