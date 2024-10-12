# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     test.py  
   Description :  
   Author :       JHao
   date：          2017/3/7
-------------------------------------------------
   Change Activity:
                   2017/3/7: 
-------------------------------------------------
"""
__author__ = 'JHao'

import redis
import requests

from test import testProxyValidator
from test import testConfigHandler
from test import testLogHandler
from test import testDbClient
# import redis

if __name__ == '__main__':
    # print("ConfigHandler:")
    # testConfigHandler.testConfig()
    #
    # print("LogHandler:")
    # testLogHandler.testLogHandler()
    #
    # print("DbClient:")
    # testDbClient.testDbClient()
    #
    # print("ProxyValidator:")
    # testProxyValidator.testProxyValidator()

    try:
        r = redis.Redis(host='127.0.0.1', port=6379, password='123456', db=0)
        for i in range(10):
            print(requests.get("http://127.0.0.1:5000/get/").json().get('proxy'))
        r.close()
    except requests.exceptions.ConnectionError as e:
        print(e)


