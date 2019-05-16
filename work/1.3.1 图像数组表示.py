# -*- coding: utf-8 -*-
"""
Created on Tue May 14 21:10:38 2019

@author: Administrator
"""

im = array(Image.open('ting.jpg'))
print(im.shape, im.dtype)
im = array(Image.open('ting.jpg').convert('L'),'f')
print(im.shape, im.dtype)