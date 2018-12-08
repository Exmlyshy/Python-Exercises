#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date    : 2018-11-29 16:59:59
'''
第 0014 题： 纯文本文件 student.txt为学生信息, 里面的内容（包括花括号）如下所示：
{
    "1":["张三",150,120,100],
    "2":["李四",90,99,95],
    "3":["王五",60,66,68]
}
'''
import xlwt




student=xlwt.Workbook(encoding='utf-8')

sheet=student.add_sheet('student')


filepath=r'student.txt'
with open(filepath,'r',encoding='utf-8') as f:
    data=f.read()
d=eval(data) #不安全，不推荐使用
if __name__=='__main__':
    row=0
    for k,v in d.items():
        i=0
        sheet.write(row,0,k)
        for column in range(1,len(v)+1):
            sheet.write(row,column,v[i])
            i+=1
        row+=1
    student.save('student.xls')
