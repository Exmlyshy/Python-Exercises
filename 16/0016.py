#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date    : 2018-11-29 18:44:40
'''
第 0016 题： 纯文本文件 numbers.txt, 里面的内容（包括方括号）如下所示：

[
    [1, 82, 65535], 
    [20, 90, 13],
    [26, 809, 1024]
]
'''
import xlwt


numbers=xlwt.Workbook(encoding='utf-8')
sheet=numbers.add_sheet('numbers')

filepath=r'numbers.txt'
with open(filepath,'r',encoding='utf-8') as f:
    data=f.read()
d=eval(data)

if __name__=='__main__':
    row=0
    for rowlist in d:
        column=0
        for number in rowlist:
            sheet.write(row,column,number)
            column+=1
        row+=1
    numbers.save('numbers.xls')