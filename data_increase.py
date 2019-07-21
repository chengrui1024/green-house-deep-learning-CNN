from PIL import Image,ImageFilter
import os
import random

#共同的母文件夹
PATH='/home/chengrui/PycharmProjects/deeplearning/greenhouse'
#各自的子文件夹
PATH1='greenhouse2'
PATH2='greenhouse3'

#输入路径与输出路径

#添加椒盐噪声
def salt_and_pepper_noise(img, proportion=0.05):
    noise_img =img
    height,width =noise_img.size
    num = int(height*width*proportion)#多少个像素点添加椒盐噪声
    for i in range(num):
        w = random.randint(0,width-1)
        h = random.randint(0,height-1)
        if random.randint(0,1) ==0:
            noise_img[h,w] =0
        else:
            noise_img[h,w] = 255
    return noise_img
#旋转180°
def rotate(img,jiaodu=random.randint(0,360)):
    img=img.rotate(jiaodu)
    return img
#镜像旋转
def transpose(img):
    img=img.transpose(Image.FLIP_LEFT_RIGHT)
    return img
#滤波(锐化)
def SHARPEN(img):
   img=img.filter(ImageFilter.SHARPEN)
   return img
#
def GaussianBlur(img):
   img=img.filter(ImageFilter.GaussianBlur(radius=2))
   return img
#处理函数
def process(PATH,PATH2):
  for fname in os.listdir(PATH):
    fpath = os.path.join(PATH, fname)
    img = Image.open(fpath)
    for i in range(3):
        if i==1:
            # img =salt_and_pepper_noise(img,proportion=0.05)
            img1 =rotate(img)
            img1 =SHARPEN(img1)
            fname2 = PATH2 + os.sep +str(i)+'_'+ fname
            img1.save(fname2)
        elif i==2:
            # img =salt_and_pepper_noise(img,proportion=0.05)
            img2 =rotate(img)
            img2 =transpose(img2)
            img2 =GaussianBlur(img2)
            fname2 = PATH2 + os.sep  + str(i)+ '_'+ fname
            img2.save(fname2)
        elif i==0:
            # img =salt_and_pepper_noise(img,proportion=0.05)
            img3 =rotate(img)
            img3 =transpose(img3)
            img3 =SHARPEN(img3)
            fname3 = PATH2 + os.sep + str(i)+'_'  + fname
            img3.save(fname3)
#实现一个文件目录，对应另外一个文件
def main():
    path1=os.path.join(PATH,PATH1)
    for fname in os.listdir(path1):
        path1_2=os.path.join(path1,fname)
        path2=os.path.join(PATH,PATH2)
        path2=os.path.join(path2,fname)
        process(PATH=path1_2,PATH2=path2)

if __name__ == '__main__':
    main()
