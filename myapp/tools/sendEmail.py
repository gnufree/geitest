#!coding=utf8

from email.header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib

#发送邮件  mail_to 接收方地址 subject标题  content内容
def send_mail(mail_to,subject,content):
    from_mail = 'gnufree@126.com'
    smtp = 'smtp.126.com'

    login_user = 'gnufree@126.com'
    login_pwd = '11qq~~~'

    msg = MIMEText(content)

    msg['to'] = mail_to
    msg['from'] = from_mail
    msg['subject'] = Header(subject)

    try:
        server = smtplib.SMTP(smtp)
        server.login(login_user,login_pwd)
        error=server.sendmail(from_mail,mail_to, msg.as_string())
        server.close()
        return True
    except:
        return False

