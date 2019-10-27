# -*- coding: utf-8 -*-
# @Time    : 2019/10/16 4:01 PM
# @Author  : python小学僧
# @File    : suit.py
# @Software: PyCharm
'''
邮箱如何开启授权码：https://jingyan.baidu.com/article/db55b6093fbaab4ba20a2f7d.html
HTMLTestRunner文件下载：http://tungwaiyip.info/software/HTMLTestRunner.html

'''
import unittest
import time
import os
import smtplib

from test_api import test_requests
from email_suit import HTMLTestRunner
from email.mime.text import MIMEText
from email.header import Header

to_list = ["收件人邮箱@163.com"]

#发送邮件
def send_mail(new_report):
    f = open(new_report, 'rb')
    mail_body = f.read()
    f.close()

    msg = MIMEText(mail_body, 'html', 'utf-8')
    msg['Subject'] = Header('执行结果', 'utf-8')
    msg['From'] = "username" + "<" + "执行结果" + ">"
    msg['To'] = ";".join(to_list)
    # 这里使用 简单邮件协议
    smtp = smtplib.SMTP()
    smtp.connect('smtp.163.com', 25) # 要确保能ping通该域名 ping smtp.163.com.

    smtp.login('自己的邮箱@163.com', '授权码')  # 不是你的邮箱登录密码，而是你登录成功之后设置授权码
    smtp.sendmail('自己的邮箱@163.com', to_list, msg.as_string())
    smtp.quit()
    print ('邮件已发出！注意查收。')

#======查找测试目录，找到最新生成的测试报告======

def new_report(test_report):
    lists = os.listdir(test_report)
    lists.sort(key=lambda fn: os.path.getmtime(test_report + '/' + fn))
    file_new = os.path.join(test_report, lists[-1])
    print (file_new)
    return file_new

#定义主方法
if __name__=='__main__':
    #添加单元测试到测试套件中
    suit = unittest.TestSuite()
    #添加index的单元测试
    suit.addTest(unittest.makeSuite(test_requests.server2))

    #直接添加单元测试到测试套件中
    #suit= unittest.makeSuite(registerunit.RegisterUnit,"test")
    path = os.getcwd()  # 此脚本的父级目录
    report_time = time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime())
    report_name = path + '/report/' + report_time + '-report.html'  # 报告保存路径及名称
    #写入
    with open(report_name, 'wb') as fp:
       # 生成报告未HTML格式，
       runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u'执行结果', description=u'接口用例执行情况')
       runner.run(suit)  # 开始执行生成测试报告
    #此方法是获取测试报告的所在目录路径
    new_report = new_report(path + '/report')
    #此方法根据测试报告所在目录路径发送邮件
    send_mail(new_report)

    '''
    python使用SMTP发送邮件报错：smtplib.SMTPDataError: (554, 'DT:SPM...
     在发送邮件时，在邮件的主题不要添加 类似于 test 之类的字眼，并把自己也添加为收件人，
    '''