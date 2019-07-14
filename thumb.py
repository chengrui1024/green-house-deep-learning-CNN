from PIL import Image
import os
#文件路径、resize图片的大小

PATH='/home/chengrui/图片/处理图片'
SIZE=100

def make_thumb(path, sizes=200):
    """
    sizes 参数传递要生成的尺寸，可以生成多种尺寸
    """
    base, ext = os.path.splitext(path)
    try:
        im = Image.open(path)
    except IOError:
        return
    mode = im.mode
    if mode not in ('L', 'RGB'):
        if mode == 'RGBA':
            # 透明图片需要加白色底
            alpha = im.split()[3]
            bgmask = alpha.point(lambda x: 255 - x)
            im = im.convert('RGB')
            # paste(color, box, mask)
            im.paste((255, 255, 255), None, bgmask)
        else:
            im = im.convert('RGB')

    width, height = im.size
    if width == height:
        region = im
    else:
        if width > height:
            delta = (width - height) / 2
            box = (delta, 0, delta + height, height)
        else:
            delta = (height - width) / 2
            box = (0, delta, width, delta + width)
        region = im.crop(box)


        filename = base + "_" + "%sx%s" % (str(sizes), str(sizes)) + ".jpg"
        thumb = region.resize((sizes, sizes), Image.ANTIALIAS)
        thumb.save(filename, quality=100)  # 默认 JPEG 保存质量是 75, 不太清楚。可选值(0~100)

if __name__ == '__main__':
    for fname in os.listdir(PATH):
      fpath=os.path.join(PATH,fname)
      make_thumb(fpath,sizes=SIZE)