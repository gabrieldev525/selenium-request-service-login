username = "gvictor525.gv@gmail.com"
password = "Devgab525"

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import re
import time

driver = webdriver.Chrome('/usr/bin/chromedriver')
driver.get("https://github.com/login/")


user = driver.find_element_by_name('login')
user.send_keys(username)
pswd = driver.find_element_by_name('password')
pswd.send_keys(password)

user.send_keys(Keys.ENTER)

print('wait...')
time.sleep(1)

if driver.find_elements_by_css_selector('#js-flash-container .flash-error .container'):
  print('login error')
else:
  print('login ok')

driver.quit()
