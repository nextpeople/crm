import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.utils import formataddr
import time

#============定义发送邮件============
class send_mail():
    def __init__(self):
        self.smtpserver = "smtp.qq.com"      #发件服务器
        self.port = 465                      #端口
        self.sender = "374679112@qq.com"     #发送端
        self.psw = "akggujgkzbnccadd"        #密码/授权码
        self.receiver = "1037814286@qq.com"   #接收端

    #=========编辑邮件内容=========
    def addFile(self,files):   #设置接收多个附件
        self.msg = MIMEMultipart()
        for el in files:
            if '.html' in str(el):
                f = open(el, 'rb')
                mail_body = f.read()
                body = MIMEText(mail_body, "html", "utf-8")
                f.close()
                self.msg.attach(body)  # 挂起、固定？
                att = MIMEText(mail_body, "base64", "utf-8")
                att["Content-Type"] = "application/octet-stream"
                att["Content-Disposition"] = 'attachment; filename="test_report.html"'  # 定义附件名称
                self.msg.attach(att)  # 挂起

            elif '.png' in str(el):
                img=open(el,'rb').read()
                att1 = MIMEText(img, "base64", "utf-8")
                att1["Content-Type"] = "application/octet-stream"
                att1["Content-Disposition"] = 'attachment; filename="test_shots.png"'  # 定义附件名称
                self.msg.attach(att1)  # 挂起

        self.msg["from"] = self.sender  # 发件人
        self.msg["to"] = self.receiver  # 收件人
        self.msg["subject"] = "自动化测试报告"  # 主题

    # =========发送邮件=========
    def final_send(self):
        smtp = smtplib.SMTP_SSL(self.smtpserver, self.port)
        smtp.login(self.sender, self.psw)
        smtp.sendmail(self.sender, self.receiver, self.msg.as_string())  # 发送
        smtp.quit()  # 关闭