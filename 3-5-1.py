import sys
import io
from bs4 import BeautifulSoup
import requests
from fake_useragent import UserAgent

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

#요청 url
url = 'https://www.wishket.com/accounts/login/'

#Fake User-Agent 생성
ua = UserAgent()
#print(ua.ie)
#print(ua.chrome)
#print(ua.random)
with requests.Session() as s:
    #url 연결
    s.get(url)
    #login 정보 payload
    LOGIN_INFO = {
        'identification' : '003power',
        'password' : 'pjyo9452',
        'csrfmiddlewaretoken': s.cookies['csrftoken']
    }
    #print('headers',s.headers)
    #print('token',s.cookies['csrftoken'])
    #요청
    response = s.post(url,data=LOGIN_INFO, headers={'User-Agent':str(ua.chrome), 'Referer':'https://www.wishket.com/accounts/login/'})
    #print('response', response.text)
    if response.status_code == 200 and response.ok:
        soup = BeautifulSoup(response.text, 'html.parser')
        projectlist = soup.select("div.contract-data > div.contract-data-box > div.history-body-title")
        #print(projectlist)
        for k in projectlist:
            print(k.string)
