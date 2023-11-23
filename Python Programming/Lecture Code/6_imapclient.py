'''
Naver Mailroom -> Settings -> POP3/IMAP Setting 
메일을 보낼때는 smtp로 보내지만 메일이 도착할 때는 imap으로 도착 (imap.naver.com)
993번 PORT로 지원 
'''

import imapclient  # internet message acess protocol 
import pyzmail     
from datetime import date, timedelta

# Configuration 
MYID = ""
MYPW = ""

# Login
imap = imapclient.IMAPClient('imap.naver.com', ssl=True)
imap.login(MYID, MYPW)
imap.select_folder('INBOX', readonly=False)

# 메일함에 있는 모든 메일의 id 식별 (내용 x)
mids = imap.search(['ALL'])
print(len(mids)) # number of mails 

# 오늘 온 메일 확인하기 
mids = imap.search(['ON', '2023-11-07']) 
mids = imap.search(['ON', date.today()]) 
print(mids)

# 오늘 기준 어제 온 메일 확인하기, 오늘 기준 지난 일주일 동안 받은 메일 확인하기 
mids = imap.search(['ON', date.today() - timedelta(days=1)]) 
mids = imap.search(['SINCE', date.today() - timedelta(days=7)])
#print(timedelta?)  # 도움말 볼 수 있음 

# 메일 제목 내 단어로 검색하기 
mids = imap.search(['SUBJECT', 'How'])
mids = imap.search(['SUBJECT', '광고'])

rmgsgs = mids.fetch(mids, ['BODY[]'])
print(message.get_charset('cp949'))
print(message.get_address('from'))
print(message.get_address('cc'))
