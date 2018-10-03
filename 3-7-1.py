import sys
import io
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

class NcafeWriteAtt:
    #초기화 실행(webdriver 설정)
    def __init__(self):
        chrome_options = Options()
        chrome_options.add_argument('window-size=1920x1080')
        chrome_options.add_argument("--headless")
        self.driver = webdriver.Chrome(chrome_options=chrome_options,executable_path="c:/webdriver/chrome/chromedriver")
        self.driver.implicitly_wait(5)

    #네이버 카페 로그인 % 출첵
    def writeAttendCheck(self):
        self.driver.get('https://logins.daum.net/accounts/loginform.do')
        self.driver.find_element_by_name('id').send_keys('003power')
        self.driver.find_element_by_id('inputPwd').send_keys('wlsdud12')
        self.driver.find_element_by_xpath('//*[@id="loginBtn"]').click()
        self.driver.implicitly_wait(30)
        #print('test', self.driver.page_source)
        self.driver.get('http://cafe.daum.net/_c21_/member_article_cafesearch?grpid=fjM0&fldid=&item=userid')
        self.driver.implicitly_wait(30)
        print(self.driver.page_source)

    # 소멸자
    def __del__(self):
        #self.driver.close() : 현재실행포커스된영역 종료
        self.driver.quit()  # : 셀레니움 전체 종료
        print("Removed driver Object")

#실행

if __name__ == '__main__':
    #객체생성
    a = NcafeWriteAtt()
    #시작시간
    start_time = time.time()
    #프로그램실행
    a.writeAttendCheck()
    #종료시간출력
    print("---Total %s seconds ---" % (time.time() - start_time))
    #객체소멸
    del a
