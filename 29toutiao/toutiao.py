#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date    : 2018-12-31 16:48:18
import logging
logging.basicConfig(level=logging.INFO)
import requests
import re
import json
import pymongo
import pyquery
from bs4 import BeautifulSoup
from urllib.parse import urlencode
from config import *

client=pymongo.MongoClient(MONGODB_URL)
db=client[MONGODB_DB]




headers={
    'Host': 'www.toutiao.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
}

def get_page_index(offset,keyword):
    data={
        'offset': offset,
        'format': 'json',
        'keyword': keyword,
        'autoload': 'true',
        'count': '20',
        'cur_tab': '1',
        'from': 'search_tab',
        'pd': 'synthesis'
    }
    base_url='https://www.toutiao.com/search_content/?'
    url=base_url+urlencode(data)
    resp=requests.get(url)
    return resp.text


def parse_page_url(resp):
    data=json.loads(resp)
    if data and 'data' in data:
        data=data['data']
        print(type(data))

    for item in data:
        try:
            url=item.get('article_url')
            if not (url is None):
                yield url
        except Exception:
            pass


def get_page_resp(url):
    try:
        response=requests.get(url,headers=headers)
        if response.status_code==200:
            return response.text
        return None
    except Exception as e:
        logging.info(e)
        return None


def parse_image_urls(html):
    soup=BeautifulSoup(html,'lxml')
    title=soup.select('title')[0].get_text()
    print(title)
    img_re=re.compile(r'gallery:.JSON.parse\("(.*?)"\)',re.S)
    result=img_re.search(html)
    if result:
        data=json.loads(result.group(1).replace(r'\\','\\').replace(r'\"','"'))
        if data and 'sub_images' in data:
            sub_images=data.get('sub_images')
            images=[item.get('url') for item in sub_images]
            return {
                'title':title,
                'images':images
            }

def save_to_mongo(data):
    try:
        db[MONGODB_TABLE].insert_one(data)
    except Exception as e:
        logging.info(e)
    

def main():
    resp=get_page_index(OFFSET,KEYWORD)
    for url in parse_page_url(resp):
        print(url)
        html=get_page_resp(url)
        if html:
            result=parse_image_urls(html)
            if result:
                result['url']=url
                save_to_mongo(result)

        
if __name__ == '__main__':
    main()

