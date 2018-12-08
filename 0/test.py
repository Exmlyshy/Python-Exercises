#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date    : 2018-11-26 11:18:04
from PIL import Image

with open('thumb.png','rb') as f:
    data=f.read()
print(len(data))