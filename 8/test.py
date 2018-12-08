#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date    : 2018-11-27 19:25:16
from urllib import request
import sys
from html.parser import HTMLParser
from html.entities import name2codepoint


class PythonorgHTMLParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.__parsedata = ''
        # self.endprint_flag = False

    def handle_starttag(self, tag, attrs):
        if ('class', 'event-title') in attrs:  # 判断当前tag数据名称
            self.__parsedata = 'name'
        elif tag == 'time':
            self.__parsedata = 'time'
        elif ('class', 'say-no-more') in attrs:
            self.__parsedata = 'year'
        elif ('class', 'event-location') in attrs:
            self.__parsedata = 'location'
        elif ('class', 'widget-title just-missed') in attrs:
            # self.endprint_flag = True
            sys.exit()

    def handle_endtag(self, tag):
        if tag == 'h3' or tag == 'span':
            self.__parsedata = ''

    def handle_data(self, data):

        if self.__parsedata == 'name':
            print('会议名称:%s' % data)

        elif self.__parsedata == 'time':
            print('会议时间:%s' % data)

        elif self.__parsedata == 'year':
            print('会议年份:%s' % data.strip())

        elif self.__parsedata == 'location':
            print('会议地点:%s' % data)
            print('----------------------------------')


parser = PythonorgHTMLParser()
url = 'https://www.python.org/events/python-events/'
with request.urlopen(url) as f:
    data = f.read()
parser.feed(data.decode('utf-8'))
