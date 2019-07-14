import os
#输入路径
path="/home/chengrui/PycharmProjects/deeplearning/practice/构建cnn平台/实例/大棚/大棚"
#输入添加的内容
content="1"
for file in os.listdir(path):

    newname = path+os.sep+content+ str(file)
    oldname=path+os.sep+file
    os.rename(oldname,newname)