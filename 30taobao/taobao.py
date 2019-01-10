#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date    : 2019-01-04 13:58:12
import re
from pyquery import PyQuery
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
import pymongo
from config import *

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument(
    "'User-Agent'='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/603.2.4 (KHTML, like Gecko) Version/10.1.1 Safari/603.2.4'"
)
chrome_options.add_argument('--disable-infobars')
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
chrome = webdriver.Chrome(CHROME_DRIVER, options=chrome_options)
wait = WebDriverWait(chrome, 10)
client=pymongo.MongoClient(MONGO_URL)
db=client[MONDODB]


def search():
    try:
        t_input=wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'#q')))
        submit=wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'#J_TSearchForm > div.search-button > button')))
        t_input.send_keys(KEYWORD)
        submit.click()
        total=wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'#mainsrp-pager > div > div > div > div.total')))
        get_products()
        return total.text

    except Exception as e:
        raise e

def get_page(page):
    try:
        index=wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'#mainsrp-pager > div > div > div > div.form > input')))
        submit=wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'#mainsrp-pager > div > div > div > div.form > span.btn.J_Submit')))
        index.clear()
        index.send_keys(page)
        submit.click()
        wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR,'#mainsrp-pager > div > div > div > ul > li.item.active > span'),str(page)))
        get_products()
    except Exception as e:
        raise e


def get_products():
    try:
        wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR,'#mainsrp-itemlist .items .item')))
        html=chrome.page_source
        doc=PyQuery(html)
        items=doc('#mainsrp-itemlist .items .item').items()
        for item in items:
            product={
                'title':item.find('.title').text().replace('\n',' '),
                'price':item.find('.price').text().replace('\n',' '),
                'deal':item.find('.deal-cnt').text()[:-3],
                'shop':item.find('.shop .shopname').text(),
                'image':item.find('.pic .img').attr('src'),
                'location':item.find('.location').text()
            }
            print(product)
            save_to_mongo(product)
    except Exception as e:
        raise e

def save_to_mongo(data):
    try:
        db[MONGOTABLE].insert_one(data)
        print('存储到MongoDB成功.')
    except Exception as e:
        print('存储到MongoDB失败：',e)


def main():
    chrome.get(TAOBAO_URL)
    for item in COOKIES:
        chrome.add_cookie(item)

    total=search()
    total=int(re.compile(r'(\d+)').search(total).group(1))
    print(total)
    for i in range(2,total):
        get_page(i)

if __name__ == '__main__':
    main()

