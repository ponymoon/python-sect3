import sys
import io
from bs4 import BeautifulSoup
import requests

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

#로그인 유저정보
LOGIN_INFO = {
    'user_id': '',
    'user_pw': ''
}

#session 생성, with 구문안에서 유지
with requests.Session() as s:
    login_req = s.post('', data=LOGIN_INFO)
    #html 소스 확인
    #print('login_req', login_req.text)
    #header 확인
    #print('headers', login_req.headers)
    if login_req.status_code == 200 and login_req.ok:
        post_one = s.get('')
        post_one.raise_for_status()
        soup = BeautifulSoup(post_one.text, 'html.parser')
        #print(soup.prettify())
        article = soup.select_one("").find_all('')
        #print(article)
