import time
from fujianemail import send_mail
import unittest
from HTMLTestRunner import HTMLTestRunner
import os

dir = './'
dis = unittest.defaultTestLoader.discover(dir,pattern='CRM添加员工.py')
# runner = unittest.TextTestRunner()
# runner.run(dis)
# 我们要新建一个用于保存我们测试结果的文件，html
now = time.strftime("%Y-%m-%d-%H-%M-%S")
print(now)
# 定义文件的名字
filename = './' + now + "_result.html"
print(filename)
file = open(filename, "wb")
# 执行我们的报告写入
runner = HTMLTestRunner(stream=file, title="CRM添加员工模块测试报告", description="用例执行情况:")
# stream：是指定测试报告文件
# title：指定报告的标题
# description:指定报告的副标题
# #执行我们测试用例
runner.run(dis)
time.sleep(3)
file.close()
# send_mail(filename)
sendlist=[]
mail = send_mail()  # 建立邮件连接
for i in os.listdir(r'./'):  # 遍历Report文件夹，将文件名保存在列表
    b = i.rstrip('.png')
    if b >= now:
        shotspath = r'./' + i  # 筛选大于程序开始时间的文件及截图
        sendlist.append(shotspath)
print(sendlist)
mail.addFile(sendlist)  # 添加邮件
mail.final_send()  # 建立附件


