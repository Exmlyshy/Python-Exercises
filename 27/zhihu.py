#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date    : 2018-12-06 10:47:14
import requests

r = requests.get('https://www.zhihu.com/', headers={
                 'User-Agent': 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25'})
print(r.headers)
with open('zhihu.html','wb') as f:
    f.write(r.content)
