# -*- coding: utf-8 -*-
"""
Created on Tue May 14 20:42:54 2019

@author: Administrator
"""

from PIL import Image
from pylab import *
im = array(Image.open('ting.jpg'))
imshow(im)
print('Please click 3 points')
x = ginput(3)
print('you clicked:',x)
show()