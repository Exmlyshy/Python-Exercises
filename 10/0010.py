#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date    : 2018-11-29 10:36:33
import random
import string
from PIL import Image,ImageFont,ImageFilter,ImageDraw


#背景随机颜色填充
def bgcolor1(): 

    return (random.randint(64,255),random.randint(64,255),random.randint(64,255))

#验证码随机颜色填充
def bgcolor2(): 

    return (random.randint(32,127),random.randint(32,127),random.randint(32,127))
#随即字母
def rndchar():

    return random.choice(string.ascii_uppercase)


width=240
height=60
im=Image.new('RGB',(width,height),(255,255,255))
font=ImageFont.truetype('arial.ttf',35)
draw=ImageDraw.Draw(im)

#填充每个像素
for w in range(width):
    for h in range(height):
        draw.point((w,h),fill=bgcolor1())

#生成验证码
for t in range(4):
    draw.text((60*t+10,10),rndchar(),font=font,fill=bgcolor2())

image=im.filter(ImageFilter.BLUR)
image.show()
image.save('VerificationCode.jpg')