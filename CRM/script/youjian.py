import smtplib
# smtp是一个邮件的传输协议它是来控制邮件发送的
from email.mime.text import MIMEText
from email.header import Header
# 发送到邮箱

# 定义发送发送邮箱的服务器
url ='smtp.qq.com'
# 定义发送邮箱的帐号及密码
user="1037814286@qq.com"  # 发送者
password='romzylcsmfdhbfff'  # 邮箱登录密码？
receiver="1037814286@qq.com"  # 收件者

# 定义发送的主题
subject='CRM添加员工自动化测试'

# 定义发送内容（正文）
msg=MIMEText("这是我们的第一个自动邮件")

# 定义发送的标题并且指了编码的格式
msg['subject'] = Header(subject,'utf-8')

# 连接发送邮件
smtp = smtplib.SMTP_SSL(url)  # 连接发送都邮件服务器的，端口号
smtp.login(user,password)  # 用来登录

# 由谁发送给谁
smtp.sendmail(user,receiver,msg.as_string())
smtp.quit()  # 用于结束我们SMTP的会话
