import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chromedriver=r'D:\Program Files (x86)\chromedriver_win32\chromedriver.exe'
chrome=webdriver.Chrome(chromedriver)
cookie=[
{
    "domain": ".taobao.com",
    "expirationDate": 1578136590.414736,
    "hostOnly": False,
    "httpOnly": False,
    "name": "_cc_",
    "path": "/",
    "sameSite": "no_restriction",
    "secure": False,
    "session": False,
    "storeId": "0",
    "value": "URm48syIZQ%3D%3D",
    "id": 1
},
{
    "domain": ".taobao.com",
    "hostOnly": False,
    "httpOnly": False,
    "name": "_tb_token_",
    "path": "/",
    "sameSite": "no_restriction",
    "secure": False,
    "session": True,
    "storeId": "0",
    "value": "e58d7ee3f5677",
    "id": 2
},
{
    "domain": ".taobao.com",
    "expirationDate": 2177320457,
    "hostOnly": False,
    "httpOnly": False,
    "name": "cna",
    "path": "/",
    "sameSite": "no_restriction",
    "secure": False,
    "session": False,
    "storeId": "0",
    "value": "EIQAEiL9bXMCAXAcqjkWaKPO",
    "id": 3
},
{
    "domain": ".taobao.com",
    "hostOnly": False,
    "httpOnly": True,
    "name": "cookie2",
    "path": "/",
    "sameSite": "no_restriction",
    "secure": False,
    "session": True,
    "storeId": "0",
    "value": "13aa65f53ad49d7d5bd81685cd8d6007",
    "id": 4
},
{
    "domain": ".taobao.com",
    "expirationDate": 1861960592.044389,
    "hostOnly": False,
    "httpOnly": True,
    "name": "enc",
    "path": "/",
    "sameSite": "no_restriction",
    "secure": True,
    "session": False,
    "storeId": "0",
    "value": "xkXdq2etSY7BiWEYWg2DkEh9ckMkNjjbnhOfUVVb5QCU%2F2LdpWixtf2y0BB8EfJvdxDkY8vH%2F71F7BgXuabEHQ%3D%3D",
    "id": 5
},
{
    "domain": ".taobao.com",
    "expirationDate": 1578136594.685563,
    "hostOnly": False,
    "httpOnly": False,
    "name": "hng",
    "path": "/",
    "sameSite": "no_restriction",
    "secure": False,
    "session": False,
    "storeId": "0",
    "value": "CN%7Czh-CN%7CCNY%7C156",
    "id": 6
},
{
    "domain": ".taobao.com",
    "expirationDate": 1562205388,
    "hostOnly": False,
    "httpOnly": False,
    "name": "isg",
    "path": "/",
    "sameSite": "no_restriction",
    "secure": False,
    "session": False,
    "storeId": "0",
    "value": "BIGB9DcGueCBLdNM7Pc8Xq8ckM1bBvayF8d8I-PWYAjnyqGcK_4FcK_gqD6MRo3Y",
    "id": 7
},
{
    "domain": ".taobao.com",
    "expirationDate": 1562205392,
    "hostOnly": False,
    "httpOnly": False,
    "name": "l",
    "path": "/",
    "sameSite": "no_restriction",
    "secure": False,
    "session": False,
    "storeId": "0",
    "value": "aBtyLkkYyixPDqbXCMaOIsMAC707BHZPiRFY1MaHaTEhNP4U7RXy1Kno-VwRj_qC5OUy_K-59",
    "id": 8
},
{
    "domain": ".taobao.com",
    "expirationDate": 1549192590.414701,
    "hostOnly": False,
    "httpOnly": False,
    "name": "lgc",
    "path": "/",
    "sameSite": "no_restriction",
    "secure": False,
    "session": False,
    "storeId": "0",
    "value": "caoheng0420",
    "id": 9
},
{
    "domain": ".taobao.com",
    "expirationDate": 1547205394.611731,
    "hostOnly": False,
    "httpOnly": False,
    "name": "mt",
    "path": "/",
    "sameSite": "no_restriction",
    "secure": False,
    "session": False,
    "storeId": "0",
    "value": "ci=31_1",
    "id": 10
},
{
    "domain": ".taobao.com",
    "expirationDate": 1554376590.414303,
    "hostOnly": False,
    "httpOnly": False,
    "name": "t",
    "path": "/",
    "sameSite": "no_restriction",
    "secure": False,
    "session": False,
    "storeId": "0",
    "value": "ad50601bd7c910888c6ba24b6caf8e9f",
    "id": 11
},
{
    "domain": ".taobao.com",
    "expirationDate": 1600600590.414834,
    "hostOnly": False,
    "httpOnly": False,
    "name": "tg",
    "path": "/",
    "sameSite": "no_restriction",
    "secure": False,
    "session": False,
    "storeId": "0",
    "value": "0",
    "id": 12
},
{
    "domain": ".taobao.com",
    "expirationDate": 1577704594,
    "hostOnly": False,
    "httpOnly": False,
    "name": "thw",
    "path": "/",
    "sameSite": "no_restriction",
    "secure": False,
    "session": False,
    "storeId": "0",
    "value": "cn",
    "id": 13
},
{
    "domain": ".taobao.com",
    "expirationDate": 1578136590.41467,
    "hostOnly": False,
    "httpOnly": False,
    "name": "tracknick",
    "path": "/",
    "sameSite": "no_restriction",
    "secure": False,
    "session": False,
    "storeId": "0",
    "value": "caoheng0420",
    "id": 14
},
{
    "domain": ".taobao.com",
    "expirationDate": 1549192590.414601,
    "hostOnly": False,
    "httpOnly": True,
    "name": "uc3",
    "path": "/",
    "sameSite": "no_restriction",
    "secure": False,
    "session": False,
    "storeId": "0",
    "value": "vt3=F8dByRItv2k1%2Fxy0AxE%3D&id2=UoH%2B4N1DneQzwQ%3D%3D&nk2=AHtyMcVY2mEQumw%3D&lg2=VFC%2FuZ9ayeYq2g%3D%3D",
    "id": 15
},
{
    "domain": ".taobao.com",
    "hostOnly": False,
    "httpOnly": False,
    "name": "v",
    "path": "/",
    "sameSite": "no_restriction",
    "secure": False,
    "session": True,
    "storeId": "0",
    "value": "0",
    "id": 16
},
{
    "domain": ".taobao.com",
    "expirationDate": 1578136598,
    "hostOnly": False,
    "httpOnly": False,
    "name": "x",
    "path": "/",
    "sameSite": "no_restriction",
    "secure": False,
    "session": False,
    "storeId": "0",
    "value": "e%3D1%26p%3D*%26s%3D0%26c%3D0%26f%3D0%26g%3D0%26t%3D0",
    "id": 17
}
]

chrome.get('https://www.taobao.com/')
for item in cookie:
    chrome.add_cookie(item)
t_input = chrome.find_element_by_css_selector('#q')
t_input.send_keys('衣服')
t_input.submit()
time.sleep(5)
chrome.quit()