#!/usr/bin/env python
#-*- coding:utf8 -*-

'''
copyright @wangxiaojie 2020.03.24
author: wangxiaojie
tip: 本代码为学习代码，并非原创，引用自《Python Cookbook（第3版）中文版》
'''

## 第11章 网络和Web编程 ##

import os, sys
from socket import socket, AF_INET, SOCK_STREAM
import time

if __name__ == "__main__":
    s = socket(AF_INET, SOCK_STREAM)
    s.connect(('localhost', 20000))
    while True: 
        time.sleep(5)
        s.send(b'Hello haha')
        msg = s.recv(8192)
        print(msg)