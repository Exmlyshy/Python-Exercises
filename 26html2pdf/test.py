#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date    : 2018-12-04 10:29:08
from urllib import request


url = 'https://www.csdn.net/'
url2='https://www.baidu.com/'
req=request.Request(url2)
req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
proxy = request.ProxyHandler({'HTTPS': '114.99.31.129:34596'})
opener = request.build_opener(proxy)
with opener.open(req) as f:
    print(f.info())
