#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date    : 2018-11-25 17:13:20
from PIL import Image,ImageDraw,ImageFont
import random

im=Image.open('user.png')
font=ImageFont.truetype('Inkfree.ttf',36)
draw=ImageDraw.Draw(im)
w,h=im.size
draw.text((w*0.8,h*0.01),str(random.randint(0,99)),font=font,fill=(255,0,0))
im.show()
im.save('0000.png')