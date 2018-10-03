import sys
import io
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

class Ncafeextr:
    #초기화 실행(webdriver 설정)
    def __init__(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        self.driver = webdriver.Chrome(chrome_options=chrome_options,executable_path="C:/webdriver/chrome/chromedriver")
        self.driver.implicitly_wait(5)

        #네이버 카페 추출

    def getMemberlist(self):
        self.driver.get('https://nid.naver.com/nidlogin.login')
        self.driver.find_element_by_name('id').send_keys('003power')
        self.driver.find_element_by_name('pw').send_keys('pjy7940900')
        self.driver.find_element_by_xpath('//*[@id="frmNIDLogin"]/fieldset/input').click()
        self.driver.get('https://cafe.naver.com/CafeProfileView.nhn?clubid=13434008')
        self.driver.implicitly_wait(30)
        self.driver.switch_to_frame('cafe_main')
        self.driver.implicitly_wait(5)
        self.driver.switch_to_frame('innerframe')
        soup = BeautifulSoup(self.driver.page_source,'html.parser')
        return soup.select('div.mem_wrap > div.mem_list div.ellipsis.m-tool-c') #자식 떨어져있으면 > 안쓰고 띄어쓴다

    def printMemberlist(self,list):
        f = open("c:/memberlist.txt", 'wt')
        for i in list:
            f.write(i.string.strip()+"/n")
            print(i.string.strip())
        f.close()

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
    a.printMemberlist(a.getMemberlist())
    #종료시간출력
    print("---Total %s seconds ---" % (time.time() - start_time))
    #객체소멸
    del a
