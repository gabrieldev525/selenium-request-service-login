username = "gvictor525.gv@gmail.com"
password = "gabriel525"

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import re
import time

driver = webdriver.Chrome('/usr/bin/chromedriver')
driver.get("https://www.linkedin.com/uas/login?_l=pt")


user = driver.find_element_by_id('username')
user.send_keys(username)

pswd = driver.find_element_by_id('password')
pswd.send_keys(password)

pswd.send_keys(Keys.ENTER) #login

print('wait...')
time.sleep(2)

if driver.find_elements_by_css_selector(".form__input--error"):
  print('login error')
else:
  print('login ok')

# driver.quit()
