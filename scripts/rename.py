import os
from os import listdir
from pathlib import Path

i = 53 #start value - 1
previous_file_name = ""
files_path = (r"C:\Users\JannesPC\Downloads\T4_resized_labeled\T4_resized")
renamed_files_path = files_path + '_renamed'
os.mkdir(renamed_files_path)

for filenames in os.listdir(files_path):
    filename, file_extension = os.path.splitext(filenames)
    if previous_file_name != (files_path + "/" + filename + ".jpg"):   
        i = i + 1
    os.rename(files_path + "/" + filenames, renamed_files_path + "/" + "tomato-" + str(i) + file_extension)
    previous_file_name = files_path + "/" + filenames


    



