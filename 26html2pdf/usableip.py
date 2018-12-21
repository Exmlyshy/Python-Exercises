#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date    : 2018-12-05 09:51:56
import random
import time
from urllib import request
from bs4 import BeautifulSoup
import requests


def iptest(url, proxies):
    usable_ip = []
    req = request.Request(url)
    req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
    for i in range(len(proxies)):
        try:
            proxy_handler = request.ProxyHandler(
                {proxies[i][0].lower(): proxies[i][1]})
            print(str({proxies[i][0].lower: proxies[i][1]}))
            opener = request.build_opener(proxy_handler)
            r = opener.open(url, timeout=2)
            print(r.info())
            usable_ip.append(proxies[i])
        except:
            print('failed.')
            continue
    return usable_ip


def get_ip(url):

    ip_list = []
    req = request.Request(url)
    req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
    r = request.urlopen(req)
    soup = BeautifulSoup(r.read(), 'html.parser')
    tr_tags = soup.find_all('tr')[1:]
    for tr_tag in tr_tags:
        ip = []
        td_tags = tr_tag.find_all('td')
        ip.append(td_tags[5].text)
        addr = td_tags[1].text + ':' + td_tags[2].text
        ip.append(addr)
        ip_list.append(ip)
    return ip_list


if __name__ == '__main__':
    url = 'http://www.xicidaili.com/nn/'
    testurl='https://www.baidu.com/'
    ip_lists=[]
    for i in range(1):
        ip = get_ip(url + str(random.randint(1, 40)))
        ip_lists.extend(ip)
    usableIP=iptest(testurl,ip_lists)
    print(len(ip_lists))
    print(len(usableIP))
    with open('usableIP.txt','w') as f:
        f.write(str(usableIP))

