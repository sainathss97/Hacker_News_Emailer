import requests
from bs4 import BeautifulSoup
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import datetime

now = datetime.datetime.now()

content =''

# extract hacker news
def extract_news(url):
    print('Extracting Hacker News Stories.......')
    cnt=''
    cnt+=('<b> TOP STORIES  </b>\n'+'<br>'+ '-'*50+'<br>')
    response = requests.get(url)
    content = response.content
    soup = BeautifulSoup(content,'html.parser')
    for i,tag in enumerate(soup.find_all('td',attrs={'class':'title'  , 'valign':'' })):
        cnt+= ((str(i+1)+' :: '+tag.text+'\n'+'<br>') if tag.text!='More' else'')
        # print(tag.prettify)
    return (cnt)
cnt = extract_news('https://news.ycombinator.com/')
content+= cnt
content += ('<br> -------------------------- <br>')
content += ('<br> <br> End Of Message! ')

print(f"{'<' * 5}Email generation in progress{'>'*5}")


# sending email

SERVER = 'smtp.gmail.com'
PORT = 587
FROM = 'foundmenobody@gmail.com'
TO = 'sainath.ss97@gmail.com'
PASS = '05051997sai'

msg =MIMEMultipart()

msg['Subject'] = f'Automated News {"-"*5} Headlines {"-"*5} {str(now.day) + "/"+str(now.month)+"/"+str(now.year)+"-"*5 }'
msg['From'] =FROM
msg['TO']  = TO
msg.attach(MIMEText(content,'html'))

print(f'{"*"*10}  Intialising server {"*"*10}')

server = smtplib.SMTP(SERVER,PORT)
server.set_debuglevel(1)
server.ehlo()
server.starttls()
server.login(FROM,PASS)
server.sendmail(FROM,TO,msg.as_string())
print(msg.as_string())
print(f"{'*'*10} Email Sent {'*'*10}")
server.quit()