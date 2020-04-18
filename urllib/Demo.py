#!/usr/bin/env python
#-*- coding:utf8 -*-

'''
copyright @wangxiaojie 2020.03.24
author: wangxiaojie
tip: 本代码为学习代码，并非原创，引用自《Python Cookbook（第3版）中文版》
'''

## 第11章 网络和Web编程 ##

import os, sys
from urllib import request, parse

if __name__ == "__main__":
    #Get请求
    url = 'http://httpbin.org/get'
    parms = {
        'name1': 'value1',
        'name2': 'value2'
    }
    querystring = parse.urlencode(parms)
    u = request.urlopen(url + '?' + querystring)
    resp = u.read()
    print(resp)

    #Post请求
    url = 'http://httpbin.org/post'
    parms = {
        'name1': 'value1',
        'name2': 'value2'
    }
    querystring = parse.urlencode(parms)
    u = request.urlopen(url, querystring.encode('ascii'))
    resp = u.read()
    print(resp)

    #Extra headers
    headers = {
        'User-agent': 'none/ofyourbusiness',
        'Spam': 'Eggs'
    }
    req = request.Request(url, querystring.encode('ascii'), headers=headers)
    u = request.urlopen(req)
    resp = u.read()
    print(resp)