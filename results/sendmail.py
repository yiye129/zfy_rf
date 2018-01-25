# -*- coding: utf-8 -*-
#encoding=utf-8


import time
import smtplib
import email
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import sys
from bs4 import BeautifulSoup
import os.path 
reload(sys)
sys.setdefaultencoding('utf-8')

#如果是list请以逗号分隔
mailto_list=['qiuxy@cdhncy.com','315811821@qq.com']
mail_host="smtp.exmail.qq.com"
mail_user="qiuxy@cdhncy.com"
mail_pass="Qxy888"
mail_postfix="cdhncy.com"
sender = 'qiuxy@cdhncy.com'

def send_mail(open_file, attfile1, attfile2):

    msg = MIMEMultipart()
    msg['Subject'] = "RF报告邮件发送测试"
    msg['From'] = "发送人：邱小叶"
    msg['To'] = "接收者：邱小叶"

    #fp = open(r'D:\pythonrf\sample\testReport\log.html',"r")
    fp = open(open_file,"r")
    content = fp.read()
    msg.attach(MIMEText(content, _subtype='html', _charset='utf-8'))
    fp.close()


    #log report
    #att1 = MIMEText(open(r'D:\pythonrf\sample\testReport\log.html', 'rb').read(), 'base64', 'gb2312')
    att1 = MIMEText(open(attfile1, 'rb').read(), 'base64', 'gb2312')
    att1["Content-Type"] = 'application/octet-stream'
    att1["Content-Disposition"] = 'attachment; filename="report.html"'
    msg.attach(att1)

    #result report
    #att2 = MIMEText(open(r'D:\pythonrf\sample\testReport\report.html', 'rb').read(), 'base64', 'gb2312')
    att2 = MIMEText(open(attfile2, 'rb').read(), 'base64', 'gb2312')
    att2["Content-Type"] = 'application/octet-stream'
    att2["Content-Disposition"] = 'attachment; filename="log.html"'
    msg.attach(att2)


    try:
        server = smtplib.SMTP()
        server.connect(mail_host)
        server.login(mail_user,mail_pass)
        server.sendmail(sender, mailto_list, msg.as_string())
        server.close()
        return True
    except Exception, e:
        print str(e)
        return False

if __name__ == '__main__':  
    if send_mail(r'log.html', r'log.html', r'report.html'):
        print u"发送成功"
    else:  
        print u"发送失败"
    '''today = time.strftime('%Y-%m-%d',time.localtime(time.time()))
    detailTime = time.strftime('%H:%M:%S',time.localtime(time.time()))
    print today,detailTime
    soup = BeautifulSoup(open("D:/pythonrf/sample/testReport/reportlog.html",'rb+'),"html.parser")
    print soup
    body = soup.find("body")
    runPassRate =  body.find("td").string
    print runPassRate.split(" ")[3]'''