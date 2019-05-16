# -*- coding: utf-8 -*-
"""
Created on Tue May 14 19:36:36 2019

@author: Administrator
"""
from PIL import Image
pil_im = Image.open('timg.jpg')
pil_im.thumbnail((128,128))
pil_im.show()



