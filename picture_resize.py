import os
import glob
from PIL import Image

dir_picture = str(input('Please enter the path of the file to be processed'))
files = glob.glob(dir_picture + '/*.png')
convert_picture = dir_picture + '/convert/'
os.makedirs(convert_picture, exist_ok= True)

print(dir_picture)
print(files)

for f in files:
    img = Image.open(f)
    img_resize = img.resize((int(img.width / 4), int(img.height / 4)))
    title, ext = os.path.split(f)
    img_resize.save(convert_picture + os.path.basename(f))