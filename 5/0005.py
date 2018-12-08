#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date    : 2018-11-26 10:28:05
'''
第 0005 题： 你有一个目录，装了很多照片，把它们的尺寸变成都不大于 iPhone5 分辨率的大小。
ip5分辨率：1136x640
图片应保持宽高比
'''
import os

from PIL import Image,ImageDraw


ip5_w,ip5_h=640,1136

files=os.listdir('.')
ext=['jpg','jpeg','png','bmp']

def process_img(im,name):
	im.thumbnail((ip5_w,ip5_h))#thumbnail()函数会保持原图宽高比,并取(width,height)中按比例更小者缩小，不会放大
	# namelist=name.split('.')
	# im.save(''.join(namelist[:-1])+'_thumb.'+namelist[-1])
	im.save('_thumb'.join(os.path.splitext(name)))



for file in files:
	if file.split('.')[-1] in ext:
		try:
			print(file)
			im=Image.open(file)
			process_img(im,file)
		except Exception as e:
			raise e
			
