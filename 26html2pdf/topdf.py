#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date    : 2018-12-04 13:05:52
import pdfkit
import os

htmls=[]
timedict={}

def sort(file):
    return os.path.getctime(file)


for file in os.listdir('.'):
    if file.split('.')[-1]=='html':
        htmls.append(file)
htmls=sorted(htmls,key=sort)
print(htmls)


options = {
            'page-size': 'Letter',
            'margin-top': '0.75in',
            'margin-right': '0.75in',
            'margin-bottom': '0.75in',
            'margin-left': '0.75in',
            'encoding': "UTF-8",
            'custom-header': [
                ('Accept-Encoding', 'gzip')
            ],
            'cookie': [
                ('cookie-name1', 'cookie-value1'),
                ('cookie-name2', 'cookie-value2'),
            ],
            'outline-depth': 10,
        }

pdfkit.from_file(htmls,'python.pdf',options=options)