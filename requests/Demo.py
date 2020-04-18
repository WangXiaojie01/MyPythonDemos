#!/usr/bin/env python
#-*- coding:utf8 -*-

'''
copyright @wangxiaojie 2020.03.24
author: wangxiaojie
tip: 本代码为学习代码，并非原创，引用自《Python Cookbook（第3版）中文版》
'''

## 第11章 网络和Web编程 ##

import os, sys
import requests

if __name__ == "__main__":
    #Post请求
    url = 'http://httpbin.org/post'
    parms = {
        'name1': 'value1',
        'name2': 'value2'
    }
    headers = {
        'User-agent': 'none/ofyourbusiness',
        'Spam': 'Eggs'
    }
    resp = requests.post(url, data=parms, headers = headers)
    print("text is %s" % resp.text)
    print("json is %s" % resp.json)
    print("content is %s" % resp.content)

    resp = requests.head('http://www.python.org/index.html')
    status = resp.status_code
    print("status is %s" % status)
    server = resp.headers['server']
    date = resp.headers['date']
    content_length = resp.headers['content-length']
    print("server is %s" % server)
    print("date is %s" % date)
    print("content_length is %s" % content_length)

    resp = requests.get('http://pypi.python.org/pypi?:action=login', auth = ('user', 'password'))
    print("status_code is %s" % resp.status_code)

    url = "http://httpbin.org/get?name=test&pass=test11"
    resp1 = requests.get(url)
    print("cookies is %s"%resp1.cookies)
    #resp2 = requests.get(url, cookies = resp1.cookies)