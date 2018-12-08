#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date    : 2018-11-29 18:31:11
'''
第 0015 题： 纯文本文件 city.txt为城市信息, 里面的内容（包括花括号）如下所示：

{
    "1" : "上海",
    "2" : "北京",
    "3" : "成都"
}
'''
import xlwt



city=xlwt.Workbook(encoding='utf-8')
sheet=city.add_sheet('city')


filepath=r'city.txt'
with open(filepath,'r',encoding='utf-8') as f:
    data=f.read()

d=eval(data)
row=0
for k,v in d.items():
    sheet.write(row,0,k)
    sheet.write(row,1,v)
    row+=1
city.save('city.xls')

