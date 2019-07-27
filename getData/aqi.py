#!/usr/bin/env python
# -*- coding:utf-8 -*-
import json

import requests

url = {
    'hongkong': 'https://api.waqi.info/feed/hongkong/?token=b41355847ebc7785075cb880a3b9386ce8817494',
    'macau'
}

payload = ""
headers = {
    'cache-control': "no-cache"
    }

response = requests.request("GET", url, data=payload, headers=headers)

aqi = {
    '香港': 0,
    '澳门': 0,
    '台湾': 0
}
print(response.text)
# data = json.loads(str(response.text))['info']
# data_filtered = []
# for ele in data:
#     pass
# with open('water_output.json', 'w', encoding='utf-8') as jsonf:
#     print(data_filtered)
#     jsonf.write(json.dumps(data_filtered))
#     jsonf.close()