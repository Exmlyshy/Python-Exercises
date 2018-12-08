#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date    : 2018-11-27 10:07:42
'''
有个目录，里面是你自己写过的程序，统计一下你写过多少行代码。包括空行和注释，但是要分别列出来。

本题遍历上一层即python-exercises目录下所有.py文件
'''
import os


def count_code(path):
    code_lines = comment_lines = empty_lines = 0
    with open(path, 'r', encoding='utf-8', errors='ignore') as f:
        line = f.readline()
        while (line and code_lines < 100000):
            if line.startswith('#'):
                comment_lines += 1
            elif line.startswith("'''"):
                comment_lines += 1
                line = f.readline()
                while(line and not line.endswith("'''\n")):
                    comment_lines += 1
                    line = f.readline()
                comment_lines += 1
            elif line == '\n':
                empty_lines += 1
            else:
                code_lines += 1
            line = f.readline()
    return (code_lines, comment_lines, empty_lines)


def count_codes(path, name_ext):
    code_lines = comment_lines = empty_lines = 0
    for root, dirs, files in os.walk(path):
        for name in files:
            # if name_ext in name:
            if name.endswith(name_ext):
                print(os.path.join(root, name))
                code_tmp, comment_tmp, empty_tmp = count_code(
                    os.path.join(root, name))
                code_lines += code_tmp
                comment_lines += comment_tmp
                empty_lines += empty_tmp
    print('code_lines:%s \ncomment_lines:%s \nempty_lines:%s ' %
          (code_lines, comment_lines, empty_lines))
    return (code_lines, comment_lines, empty_lines)


if __name__ == '__main__':
    path = input('请输入路径：')
    ext = input('请输入文本文件扩展名:')
    count_codes(path, ext)
