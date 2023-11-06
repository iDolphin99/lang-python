import smtplib
from email.mime.text import MIMEText 
from email.header import Header

# private configuration 
myid = "" 
mypw = "" 
sender = ""
receiver = ""

# 기본 프로토콜 작동 방식 
smtp = smtplib.SMTP('smtp.naver.com', 587)
print(smtp.ehlo())
print(smtp.starttls())
print(smtp.login(myid, mypw))

# 이메일 보내기 Naver -> Gmail 
subject = '이메일 보내기 test'
message = '''
testing...
testingg...
testinggg....
'''
msg = MIMEText(message.encode('utf-8'), _subtype='plain', _charset='utf-8')
msg['From'] = sender
msg['To'] = receiver
print(msg.as_bytes())

smtp.sendmail(sender, receiver, msg.as_string())
smtp.quit()