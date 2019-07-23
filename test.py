# coding=utf-8

import tensorflow as tf
import numpy as np
import pdb
from datetime import datetime
from VGG16 import *
import cv2
import os
#类别数
n_cls = 17

def test(path):
    x = tf.placeholder(dtype=tf.float32, shape=[None, 224, 224, 3], name='input')
    keep_prob = tf.placeholder(tf.float32)
    output = VGG16(x, keep_prob, n_cls)
    score = tf.nn.softmax(output)
    f_cls = tf.argmax(score, 1)

    sess = tf.InteractiveSession()
    sess.run(tf.global_variables_initializer())
    saver = tf.train.Saver()
    saver.restore(sess, '/home/chengrui/PycharmProjects/deeplearning/greenhouse/model/model.ckpt-99')
    #加入字典
    label_name_dict={
        0:"大棚",
        1: "机场",
        2: "大桥",
        3: "商业区",
        4: "沙漠",
        5: "农田",
        6: "足球场",
        7: "森林",
        8: "工业区",
        9: "草地",
        10: "山地",
        11: "公园",
        12: "停车场",
        13: "码头",
        14: "居民区",
        15: "河流",
        16: "花",
    }
    for i in os.listdir(path):
        imgpath = os.path.join(path, i)
        im = cv2.imread(imgpath)
        im = cv2.resize(im, (224, 224))  # * (1. / 255)
        im = np.expand_dims(im, axis=0)
        # pred = sess.run(f_cls, feed_dict={x:im, keep_prob:1.0})
        pred, _score = sess.run([f_cls, score], feed_dict={x: im, keep_prob: 1.0})
        prob = round(np.max(_score), 4)
        # print "{} flowers class is: {}".format(i, pred)
        pred_label=label_name_dict[int(pred)]
        print("图像名称{} ；该图像所属于类别: {}；该类别所属概率: {}%".format(i, pred_label, prob*100))
    sess.close()


if __name__ == '__main__':
    path = './test'
    test(path)


