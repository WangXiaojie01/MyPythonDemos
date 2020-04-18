#!/usr/bin/env python
#-*- coding:utf8 -*-

'''
copyright @wangxiaojie 2020.03.24
author: wangxiaojie
tip: 本代码为学习代码，并非原创，引用自《Python Cookbook（第3版）中文版》
'''

## 第11章 网络和Web编程 ##

import os, sys
from socketserver import BaseRequestHandler, TCPServer
#from socketserver import StreamRequestHandler, TCPServer
from socketserver import ThreadingTCPServer


class EchoHandler(BaseRequestHandler):
    def handle(self):
        print('Got connection from', self.client_address)
        while True:
            msg = self.request.recv(8192)
            if not msg:
                break
            self.request.send(msg)
            
'''
class EchoHandler(StreamRequestHandler):
    def handle(self):
        print("Got connect from ", self.client_address)
        for line in self.rfile:
            self.wfile.write(line)
            '''

if __name__ == "__main__":
    '''
    #serv = TCPServer(('', 20000), EchoHandler)
    serv = ThreadingTCPServer(('', 20000), EchoHandler)
    serv.serve_forever()
    '''
    from threading import Thread
    NWORKERS = 5
    serv = TCPServer(('', 20000), EchoHandler)
    for n in range(NWORKERS):
        t = Thread(target=serv.serve_forever)
        t.daemon = True
        t.start()
    serv.serve_forever()

    