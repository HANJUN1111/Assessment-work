# -*- coding: utf-8 -*-
"""
Created on Tue May 14 21:34:18 2019

@author: Administrator
"""
from PIL import Image
from numpy import *
im = array(Image.open('ting.jpg').convert('L'))
im3 = (100.0/255) * im + 100 # 将图像像素值变换到 100...200 区间
pil_im = Image.fromarray(uint8(im3))
imshow(pil_im)
show()