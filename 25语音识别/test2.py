#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date    : 2018-12-02 17:29:49
import requests
import json
import base64
import wave



base_url="https://openapi.baidu.com/oauth/2.0/token?grant_type=client_credentials&client_id=%s&client_secret=%s"
APIKey="LZAdqHUGC56WYmI6w7lmbfKm"
SecretKey="WYPPwgHuKAVpoKCiK3es9FBU6GM3VOt1"

host=base_url%(APIKey,SecretKey)


res=requests.post(host)
# print(res.json()['access_token'])
TOKEN=res.json()['access_token']

FORMAT='wav'
RATE='16000'
CHANNEL=1
CUID='Exmylyshy'

with open('16k.wav','rb') as f:
    speech_data=f.read()
SPEECH=base64.b64encode(speech_data).decode('utf-8')
data={
    'format':FORMAT,
    'rate':RATE,
    'channel':CHANNEL,
    'cuid':CUID,
    'len':len(speech_data),
    'speech':SPEECH,
    'token':TOKEN
}
url='https://vop.baidu.com/server_api'
headers = { 'Content-Type' : 'application/json'}
# r=requests.post(url,data=json.dumps(data),headers=headers)
r=requests.post(url,json=data,headers=headers)
result=r.json()['result'][0]
print(result)
