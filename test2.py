# coding=utf-8

import tensorflow as tf
import numpy as np
import pdb
from datetime import datetime
from VGG16 import *
import cv2
import os

n_cls = 4  # 输出层的个数

def test(path):
    x = tf.placeholder(dtype=tf.float32, shape=[None, 224, 224, 3], name='input')
    keep_prob = tf.placeholder(tf.float32)
    output = VGG16(x, keep_prob, n_cls)
    score = tf.nn.softmax(output)
    f_cls = tf.argmax(score, 1)

    sess = tf.InteractiveSession()
    sess.run(tf.global_variables_initializer())
    saver = tf.train.Saver()
    saver.restore(sess, '/home/chengrui/PycharmProjects/deeplearning/greenhouse/model/model.ckpt-130')
    a = 0
    b = 0
    for i in os.listdir(path):
        imgpath = os.path.join(path, i)
        im = cv2.imread(imgpath)
        im = cv2.resize(im, (224, 224))  # * (1. / 255)
        im = np.expand_dims(im, axis=0)
        # pred = sess.run(f_cls, feed_dict={x:im, keep_prob:1.0})
        pred, _score = sess.run([f_cls, score], feed_dict={x: im, keep_prob: 1.0})
        prob = round(np.max(_score), 4)
        # print "{} flowers class is: {}".format(i, pred)
        print("{} flowers class is: {}, score: {}".format(i, int(pred), prob))

        if int(pred)==1:
            a+=1

        b+=1
        print(a)
        print(b)

    sess.close()


if __name__ == '__main__':
    path = './test'
    test(path)


