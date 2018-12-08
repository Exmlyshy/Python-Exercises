#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date    : 2018-11-29 13:50:58
from urllib import request
import re


def getImgUrl(html):
    re_str=re.compile(r'class="BDE_Image" src="(.+?\.jpg)')
    url_list=re_str.findall(html)
    return url_list


if __name__=='__main__':
    url='http://tieba.baidu.com/p/2166231880?see_lz=1'
    with request.urlopen(url) as f:
        data=f.read()
    url_list_=getImgUrl(data.decode('utf-8'))
    print(len(url_list_))
    # print(url_list_[:10])
    i=0
    for imgurl in url_list_:
        try:
            print('Downloading %s.jpg...'%i)
            request.urlretrieve(imgurl,'%s.jpg'%i)
            i+=1
        except Exception as e:
            raise e
