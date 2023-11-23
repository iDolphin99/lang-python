import glob 
from PIL import Image

# 날짜별로 폴더 만들어서 사진 분류하기 
root = './Python Programming/sample_imgs'
flist = glob.glob(root + '/*.jpg')
for fpath in flist:
    img = Image.open(fpath)
    exif = img._getexif()
    folder = '-'.join(exif[0x9003].split()[0].split(':')[:2])
    fname = os.path.basename(fpath)
    folder_dst = os.path.join(root, folder)
    fpath_dst = os.paht.join(root, folder, fname)
    print(fpath, fpath_dst)
    if no os.path.exists(folder_dst):
        os.makedirs(folder_dst)
    shutil.copyfile(fpath, fpath_dst)
    print(fpath_dst)