# -*- coding: utf-8 -*-
"""
Created on Wed May 15 09:43:11 2019

@author: Administrator
"""

from numpy import *
from PIL import Image
from pylab import *
from imtools import pca
import pickle

im2 = '666.jpg'

imlist = [im2,im2,im2,im2,im2,im2,im2,im2]

im = array(Image.open(imlist[0]))
imshow(im)
m,n = im.shape[0:2]
imnbr = len(imlist)
immatrix = array([array(Image.open(im).convert('L')).flatten() for im in imlist],'f')
print(imlist)
# 执行PCA操作
V,S,immean = pca(immatrix)
# 显示一些图像
figure()
gray()
subplot(2,4,1)
imshow(immean.reshape(m,n))
for i in range(7):
    subplot(2,4,i+2)
    imshow(immean.reshape(m, n))
    imshow(V[i].reshape(m,n))
show()

print(immean)
print(V)

with open('test.jpg','wb+') as f:
     pickle.dump(immean,f)
     pickle.dump(V,f)
# 打开文件
with open('test.txt', 'rb') as f:
     immean = pickle.load(f)
     V = pickle.load(f)
     print('读取到保存的immean和V的值-------------')
     print(immean)
     print(V)
