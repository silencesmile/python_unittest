# -*- coding: utf-8 -*-
# @Time    : 2019/10/12 5:57 PM
# @Author  : python小学僧
# @File    : test_mathfunc.py
# @Software: PyCharm

import unittest
from test_func.mathfunc import *

class TestMathFunc(unittest.TestCase):
    """Test mathfuc.py"""

    def test_add(self):
        ''' test method add(a,b)'''
        self.assertEqual(3, add(1, 2))
        self.assertNotEqual(3, add(2,2))

    def setUp(self):
        ''' 测试方法的前被执行-准备工作'''
        print('setUp...')

    def tearDown(self):
        ''' 测试方法的后被执行-收尾工作：关闭数据库等'''
        print('tearDown...')


if __name__ == '__main__':
    unittest.main()