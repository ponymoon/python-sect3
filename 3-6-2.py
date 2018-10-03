import sys
import io
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

firefox_options = Options()
firefox_options.add_argument("--headless") #CLI

driver = webdriver.Firefox(firefox_options=firefox_options, executable_path='C:\\webdriver\\firefox\\geckodriver') #대문자 소문자주의!!
#driver.set_window_size(1920,1080)
driver.implicitly_wait(5)

driver.get('https://google.com')
driver.save_screenshot("c:/webdriver/website_ff1.png")

driver.implicitly_wait(5)

driver.get('https://www.daum.net/')
#time.sleep(5)
driver.save_screenshot("c:/webdriver/website_ff2.png")
driver.quit()

print('스크린샷 완료')
