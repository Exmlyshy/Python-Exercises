#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date    : 2018-12-02 11:04:25
import xlrd
import re


def count_times(time_list):
    time_re=re.compile(r'[时分秒]')
    hours=minutes=seconds=0
    for time in time_list:
        l=time_re.split(time)
        if '时' in time:
            hours+=int(l[0])
            minutes+=int(l[1])
            seconds+=int(l[2])
        elif '分' in time:
            minutes+=int(l[0])
            seconds+=int(l[1])
        elif '秒' in time:
            seconds+=int(l[0])
        else:
            continue
    if seconds>=60:
        minutes=minutes+seconds//60
        seconds=seconds%60

    if minutes>=60:
        hours=minutes//60
        minutes=minutes%60
    print('%s时%s分%s秒'%(hours,minutes,seconds))


workbook=xlrd.open_workbook('MyRecord.xlsx')

sheet_names=workbook.sheet_names()

for sheet_name in sheet_names:
    sheet:xlrd.sheet.Sheet=workbook.sheet_by_name(sheet_name)
    times_list=sheet.col_values(4)
    index=times_list.index('通信时长')
    if index:
        count_times(times_list[index+1:])
