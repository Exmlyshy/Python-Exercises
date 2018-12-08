#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date    : 2018-12-03 18:59:54
import pdfkit
import requests
import re
import os
import random
import time
from bs4 import BeautifulSoup
from urllib import request


def parse_body(url,proxies):
    res = requests.get(url, headers={
                       'User-Agent': 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25'}, proxies=proxies)
    soup = BeautifulSoup(res.content, 'html.parser')
    body = soup.find_all(class_='x-wiki-content')[0]
    title = soup.find('h4').get_text()
    center_tag = soup.new_tag('center')
    title_tag=soup.new_tag('h1')
    title_tag.string=title
    center_tag.insert(0, title)
    body.insert(0, center_tag)
    html = str(body)

    # 将<img>标签中data-src(应显示的图片)链接替换给src
    def func(m):
        return ''.join([m.group(1), m.group(4), m.group(3)])

    imgre = re.compile(r'(<img.*?)(data-src)(.*?)(src)(.*?\".+?\")')
    html = imgre.sub(func, html)
    return html.encode('utf-8')
    # with open('test.html', 'wb') as f:
    #     f.write(html.encode('utf-8'))


def parse_catalog(url):
    res = requests.get(url, headers={
                       'User-Agent': 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25'})
    soup = BeautifulSoup(res.content, 'html.parser')
    catalog = soup.find_all(attrs={'id': 'x-wiki-index'})[0]
    url_tags = catalog.find_all('a')
    urls = {}
    for url_tag in url_tags:
        url = 'https://www.liaoxuefeng.com' + url_tag.get('href')
        urls[url_tag.get_text()] = url
    return urls


if __name__ == '__main__':
    htmls = []
    url = "https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000"
    urls = parse_catalog(url)
    t = time.time()
    iplist=[['HTTPS', '115.223.109.215:8010'], ['HTTPS', '180.121.128.209:3128'], ['HTTP', '182.88.4.49:8123'], ['HTTPS', '119.144.124.135:8118'], ['HTTPS', '182.88.88.153:8123'], ['HTTP', '171.37.157.89:8123'], ['HTTP', '115.46.66.29:8123'], ['HTTPS', '60.169.201.173:8010'], ['HTTP', '182.88.88.5:8123'], ['HTTPS', '182.88.186.233:8123'], ['HTTP', '121.225.26.89:3128'], ['HTTPS', '27.16.162.155:8010'], ['HTTPS', '42.59.84.86:1133'], ['HTTPS', '115.219.111.105:8010'], ['HTTPS', '182.88.90.229:8123'], ['HTTPS', '175.148.69.90:1133'], ['HTTPS', '124.134.123.189:8118'], ['HTTPS', '175.165.130.44:1133'], ['HTTP', '175.155.139.55:1133'], ['HTTPS', '171.38.26.164:8123'], ['HTTP', '171.37.152.41:8123'], ['HTTPS', '171.38.86.119:8123'], ['HTTPS', '175.148.76.53:1133'], ['HTTPS', '115.46.70.108:8123'], ['HTTPS', '121.31.192.78:8123'], ['HTTP', '110.73.9.20:8123'], ['HTTP', '115.46.70.254:8123'], ['HTTP', '115.46.65.148:8123'], ['HTTPS', '171.37.163.244:8123'], ['HTTP', '182.88.191.40:8123'], ['HTTPS', '115.223.102.62:8010'], ['HTTPS', '175.148.77.47:1133']]
    for k, v in urls.items():
        filepath = k[:3] + '.html'
        if not os.path.isfile(k+'.html'):
            print(k)
            ip=random.choice(iplist)
            proxy={ip[0]:ip[1]}
            print(proxy)
            html = parse_body(v,proxy)
            with open(filepath, 'wb') as f:
                f.write(html)
            htmls.append(filepath)
            print('OK.')
            time.sleep(0.5)
    print('%s seconds.' % (time.time() - t))
