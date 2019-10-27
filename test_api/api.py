# -*- coding: utf-8 -*-
# @Time    : 2019/10/16 10:59 AM
# @Author  : python小学僧
# @File    : api.py
# @Software: PyCharm

class URL(object):
    #测试环境的接口地址
    base_test_url ="http://127.0.0.1:8000"
    #生产环境的接口地址
    base_online_url ="https://www.api.cn"

    # get
    index = "/get1"

    # post
    post_url = "/voice_server/v1"

if __name__ == '__main__':
    import requests

    response = requests.get("http://127.0.0.1:8000/get1")
    print(response.content)