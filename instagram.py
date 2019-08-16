username = "gvictor525.gv@gmail.com"
password = "gabriel"

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import re
import time

driver = webdriver.Chrome('/usr/bin/chromedriver')
driver.get("https://www.instagram.com/accounts/login/")

driver.find_element_by_name('username').send_keys(username)
driver.find_element_by_name('password').send_keys(password)
driver.find_element_by_name('username').send_keys(Keys.ENTER)

print('wait...')
time.sleep(2)

if driver.find_elements_by_css_selector('#slfErrorAlert'):
  print('login error')
else:
  print('login ok')
