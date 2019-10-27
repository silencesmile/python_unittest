# -*- coding: utf-8 -*-
# @Time    : 2019/10/15 6:02 PM
# @Author  : python小学僧
# @File    : test_requests.py
# @Software: PyCharm

import server
import unittest
import requests
import json
from test_api.api import *

class server2(unittest.TestCase):
    def setUp(self):
        ''' 测试方法的前被执行-准备工作'''
        print('setUp...')

        # 初始化对象
        self.URL = URL()
        self.index = self.URL.base_test_url + self.URL.index
        self.post_url = self.URL.base_test_url + self.URL.post_url

    def test_get_api(self):
        ''' get 测试过程，必须以test_开头 '''
        response = requests.get(self.index)
        ret = json.loads(response.content)
        print(ret)

        self.assertTrue(isinstance(ret, dict)) # 断言 ret的类型是dict
        self.assertIn("code", ret) # 断言 code字符串包含在ret中
        self.assertEqual(ret["code"], 0) # 断言 ret["code"] == 0

    def test_post_api(self):
        ''' post 测试过程，必须以test_开头 '''
        dict_info = {"name":"小学僧", "text":"Python小学僧"}
        data_info = json.dumps(dict_info)

        response = requests.post(self.post_url, data=data_info)
        ret = json.loads(response.content)
        print(ret)

        self.assertIn("zxc", ret) # 断言 code字符串包含在ret中
        self.assertEqual(ret["zxc"], 123) # 断言 ret["code"] == 0

    def tearDown(self):
        ''' 测试方法的后被执行-收尾工作：关闭数据库等'''
        print('tearDown...')


if __name__ == '__main__':
    unittest.main()