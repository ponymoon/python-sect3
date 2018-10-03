import sys
import io
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

chrome_options = Options()
chrome_options.add_argument("-headless") #CLI
chrome_options.add_argument("–no-sandbox")
chrome_options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36")
chrome_options.add_argument("disable-gpu")
driver = webdriver.Chrome(chrome_options = chrome_options, executable_path='c:/webdriver/chrome/chromedriver') #대문자 소문자주의!!
driver.set_window_size(1920,1080)
#driver = webdriver.Chrome('c:/webdriver/chrome/chromedriver') #대문자 소문자주의!!
driver.implicitly_wait(3)

driver.get('https://nid.naver.com/nidlogin.login')#https://user.ruliweb.com/member/login')
time.sleep(1)
driver.implicitly_wait(3)

driver.find_element_by_name('id').send_keys('003power')
driver.implicitly_wait(1)
driver.find_element_by_name('pw').send_keys('pjy7940900')
driver.implicitly_wait(1)
driver.find_element_by_xpath('//*[@id="frmNIDLogin"]/fieldset/input').click() #//*[@id="login_submit"]
driver.implicitly_wait(3)
print(driver.page_source)
