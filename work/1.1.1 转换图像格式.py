# -*- coding: utf-8 -*-
"""
Created on Tue May 14 17:49:23 2019

@author: Administrator
"""

from PIL import Image
import os
filelist=os.listdir('filelist/')
for infile in filelist:
    outfile = os.path.splitext(infile)[0] + ".jpeg"
    if infile != outfile:
        try:
            Image.open('filelist/'+infile).save(outfile)
        except IOError:
            print ("cannot convert", infile)