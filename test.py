# -*- coding: UTF-8 -*-

import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart


# 第三方 SMTP 服务
mail_host="smtp.exmail.qq.com"  #设置服务器
mail_user="qiuxy@cdhncy.com"    #用户名
mail_pass="Qxy888"   #口令 

sender = 'qiuxy@cdhncy.com'
receivers = ['qiuxy@cdhncy.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
result_file = open('report.html','rb')
result_body = result_file.read()
#result_file.close()
 
# 三个参数：第一个为文本内容，第二个 plain 设置文本格式，第三个 utf-8 设置编码

message = MIMEMultipart()
body = MIMEText(result_body, 'html', 'utf-8')
message.attach(body)
message['From'] = Header("发邮件端", 'utf-8')
message['To'] =  Header("收邮件端", 'utf-8')
 
subject = 'Python SMTP 邮件测试'
message['Subject'] = Header(subject, 'utf-8')

 
 
try:
    #smtpObj = smtplib.SMTP()
    smtpObj = smtplib.SMTP_SSL(mail_host, 465) 
    #smtpObj.connect(mail_host, 465)    # 25 为 SMTP 端口号
    smtpObj.login(mail_user,mail_pass)
    smtpObj.sendmail(sender, receivers, message.as_string())
    print "邮件发送成功"
except smtplib.SMTPException:
    print "Error: 无法发送邮件"