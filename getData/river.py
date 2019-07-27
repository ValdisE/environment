#!/usr/bin/env python
# -*- coding:utf-8 -*-
import json

import requests

url = 'http://service.envicloud.cn:8082/v2/waterquality/DMFSZGLZMTU2NDEYOTYWNDG0MW==/2018/4'

payload = ""
headers = {
    'cache-control': "no-cache"
    }

response = requests.request("GET", url, data=payload, headers=headers)

print(response.text)
data = json.loads(str(response.text))['info']
data_filtered = []
for ele in data:
    if ele['point'].find('长江') != -1 or \
        ele['drainage'].find('长江') != -1 or \
        ele['section'].find('长江') != -1 or \
        ele['river'].find('长江') != -1 or \
        ele['point'].find('黄河') != -1 or \
        ele['drainage'].find('黄河') != -1 or \
        ele['section'].find('黄河') != -1 or \
        ele['river'].find('黄河') != -1 or \
        ele['point'].find('珠江') != -1 or \
        ele['drainage'].find('珠江') != -1 or \
        ele['section'].find('珠江') != -1 or \
        ele['river'].find('珠江') != -1 or \
        ele['point'].find('松花江') != -1 or\
        ele['drainage'].find('松花江') != -1 or \
        ele['section'].find('松花江') != -1 or \
        ele['river'].find('松花江') != -1:
            data_filtered.append(ele)
with open('water_output.json', 'w', encoding='utf-8') as jsonf:
    print(data_filtered)
    jsonf.write(json.dumps(data_filtered))
    jsonf.close()