#!/usr/bin/env python
# -*- coding:utf-8 -*-

import requests

url = 'http://www.mee.gov.cn/hjzl/'
header = {
    'Host': 'www.mee.gov.cn',
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'Cookie': '_gscu_97175291=64065911ouoxtw43; _gscu_1697192173=64065911o1k7f343; wdcid=2112437f4138e7e3; gwdshare_firstime=1564126474722; _gscbrs_97175291=1; _gscbrs_1697192173=1; _gscs_97175291=64133382zpp47827|pv:4; _gscs_1697192173=64133382edggsf27|pv:4; wdlast=1564133494'
}
res = requests.get(url, header, timeout=30)
print(res.content)