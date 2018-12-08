#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date    : 2018-11-25 18:26:41

import random


def rndChar():
    if random.random() > 0.5:
        return chr(random.randint(65, 90))
    return chr(random.randint(97, 122))


CodeStrList = []
for i in range(200):
    CodeStr = ''
    for j in range(10):
        CodeStr += rndChar()
    CodeStrList.append(CodeStr)



with open('JiHuoMa.txt', 'w') as f:
    f.write('\n'.join(CodeStrList))

# import random
# import string
# string.ascii_letters

# forSelect = string.ascii_letters + string.digits


# def generate_code(count, length):
#     for x in range(count):
#         Re = ""
#         for y in range(length):
#             Re += random.choices(forSelect)
#         print(Re)
