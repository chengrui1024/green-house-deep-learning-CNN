from PIL import Image
import os

PATH='/home/chengrui/PycharmProjects/deeplearning/practice/构建cnn平台/实例/大棚/建筑'
PATH2='/home/chengrui/PycharmProjects/deeplearning/practice/构建cnn平台/实例/大棚/建筑1'
#定义大小
sizes=100
for fname in os.listdir(PATH):
    fpath = os.path.join(PATH, fname)
    img= Image.open(fpath)
    width, height = img.size
    if width > height:
        delta = (width - height) / 2
        box = (delta, 0, delta + height, height)
    else:
        delta = (height - width) / 2
        box = (0, delta, width, delta + width)
    region = img.crop(box)
    thumb = region.resize((sizes, sizes), Image.ANTIALIAS)
    fname2=PATH2+os.sep+fname
    thumb.save(fname2, quality=100)