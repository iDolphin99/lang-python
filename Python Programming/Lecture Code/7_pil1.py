import glob
from PIL import Image, ExifTags

# Import images
flist = glob.glob('./Python Programming/sample_imgs/*.jpg')
fpath = flist[0]
img = Image.open(fpath)
print(img)
print(img.mode)
print(img.format)

# Resize
img.thumbnail((512, 512))
print(img)

# Get image meta data 
metadata = img._getexif()
# print(EXifTags.TAGS)
for k, v in metadata.items():
    print(k, v)