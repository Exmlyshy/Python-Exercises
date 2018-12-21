#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date    : 2018-12-05 12:36:56
import requests
from urllib import request

# s=requests.session()
# res=s.get('https://foofish.net/python-crawler-html2pdf.html')
# print(res.headers)
# req=request.Request('http://localhost:9000/')
# req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
# proxy=request.ProxyHandler(proxies={'HTTPS':'42.101.22.93:8888'})
# opener=request.build_opener(proxy)
# r=opener.open(req)
# print(r.info())
url='https://www.baidu.com'
r=request.urlopen(url)
print(type(r))

