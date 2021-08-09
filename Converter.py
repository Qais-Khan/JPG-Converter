# Import modules
import sys
import os
from PIL import Image

param1 = sys.argv[1]  # The directory with the JPG files
param2 = sys.argv[2]  # The directory you want the PNG files saved in

# Create the directory to save the files in if it does not exist
try:
    os.mkdir(f'./{param1}{param2}')
except FileExistsError:
    print('This Path Already Exists And Shall Be Used')

# Get each image, convert, and save in new directory
for x in os.scandir(param1):
    try:
        img = Image.open(f"./{param1}{x.name}")
        img.save(f"./{param1}{param2}{x.name[0:-4]}.png", "png")
        print("Done")
    except PermissionError:  # When the code encounters a directory rather than an img, it skips it
        continue
