#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date    : 2018-11-29 11:45:33
'''
第 0012 题： 敏感词文本文件 filtered_words.txt，里面的内容 和 0011题一样，当用户输入敏感词语，则用 星号 * 替换，例如当用户输入「北京是个好城市」，则变成「**是个好城市」。
'''
import re


def generateRe_str(wordlist):

    re_str = '|'.join(wordlist)
    re_str = r'.*(%s).*' % re_str
    return re_str


def getFilterd_words():
    with open('filtered_words.txt', 'r', encoding='utf-8') as f:
        word_list = f.read().split()
    return word_list

#递归输出
def filter_print(re_str,strs):
    t=re.match(re_str,strs)
    if t:
        filter_print(re_str,strs.replace(t.group(1),'**'))
    else:
        print(strs)



if __name__ == '__main__':
    # re_filter_str=r'.*('+generateRe_str(getFilterd_words())+r').*'
    re_filter_str = generateRe_str(getFilterd_words())
    print(re_filter_str)
    while True:
        word = input('请输入:')
        filter_print(re_filter_str,word)