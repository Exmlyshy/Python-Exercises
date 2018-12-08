#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date    : 2018-11-26 11:49:11
'''
你有一个目录，放了你一个月的日记，都是 txt，为了避免分词的问题，假设内容都是英文，请统计出你认为每篇日记最重要的词。

同题4获得一篇文章的每个单词出现个数，并设置一个max_word[]保存出现次数最多的词
'''
import re
import string
import os



def count_text(text,name):
    punc = string.punctuation
    WordDict = dict()
    max_times = 1
    for word in re.split(r'[\s%s]+' % punc, text.lower()):
        if word in WordDict:
            WordDict[word] += 1
            if WordDict[word] > max_times:
                max_times = WordDict[word]
                max_word = word
        else:
            WordDict[word] = 1
    return {name:(max_word,max_times)}

with open('test.py','r') as f:
    text=f.read()
    print(count_text(text,'text'))
# files=os.listdir('.')
# for file in files:  
#     with open(file, 'r') as f:
#         text = f.read()
#         print(count_text(text,file))




# for k,v in WordDict.items():
#   if int(v)>max_times:
#       max_times=int(v)
#       max_word=
