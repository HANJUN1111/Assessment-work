# -*- coding: utf-8 -*-
"""
Created on Wed May 15 10:52:15 2019

@author: Administrator
"""
from PIL import Image
from numpy import *
from scipy.ndimage import measurements,morphology
# 载入图像，然后使用阈值化操作，以保证处理的图像为二值图像
im = array(Image.open('2.jpeg').convert('L'))
im = 1*(im<128)
labels, nbr_objects = measurements.label(im)
print("Number of objects:", nbr_objects,labels)

imshow(im)

show()
