#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date    : 2018-11-25 20:24:00
'''
第 0004 题： 任一个英文的纯文本文件，统计其中的单词出现的个数。
'''
import re
import string

with open('text', 'r') as f:
    text = f.read()

punc = string.punctuation
WordDict = dict()
for word in re.split(r'[\s%s]+' % punc, text.lower()):
    if word in WordDict:
        WordDict[word] += 1
    else:
        WordDict[word] = 1
WordDict.pop('', 'cannot find')
print(WordDict)
