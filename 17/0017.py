#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date    : 2018-12-02 10:04:32
'''
将 第 0014 题中的 student.xls 文件中的内容写到 student.xml 文件中
廖雪峰python教程:
    除了解析XML外，如何生成XML呢？99%的情况下需要生成的XML结构都是非常简单的，因此，最简单也是最有效的生成XML的方法是拼接字符串：

    L = []
    L.append(r'<?xml version="1.0"?>')
    L.append(r'<root>')
    L.append(encode('some & data'))
    L.append(r'</root>')
    return ''.join(L)
    如果要生成复杂的XML呢？建议你不要用XML，改成JSON。
'''
import xlrd
import lxml


workbook=xlrd.open_workbook('student.xls')
sheet_names=workbook.sheet_names()
for sheet_name in sheet_names:
    sheet:xlrd.sheet.Sheet=workbook.sheet_by_name(sheet_name)
    print(sheet.name,sheet.nrows,sheet.ncols)
    print(sheet.row_values(0))
    print(sheet.col_values(0))