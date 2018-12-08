#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date    : 2018-11-29 11:35:46
'''
第 0011 题： 敏感词文本文件 filtered_words.txt，里面的内容为以下内容，当用户输入敏感词语时，则打印出 Freedom，否则打印出 Human Rights。
'''
import re

def generateRe_str(wordlist):

    re_str='|'.join(wordlist)
    re_str=r'.*(%s).*'%re_str
    return re_str

def getFilterd_words():
    with open('filtered_words.txt','r',encoding='utf-8') as f:
        word_list=f.read().split()
    return word_list

if __name__=='__main__':
    # re_filter_str=r'.*('+generateRe_str(getFilterd_words())+r').*'
    re_filter_str=generateRe_str(getFilterd_words())
    print(re_filter_str)
    while True:
        word=input('请输入:')
        if re.match(re_filter_str,word):
            print('Freedom')
        else:
            print('Human Rights')
        