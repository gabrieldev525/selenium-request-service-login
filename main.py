from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import ipdb
import ast
import json
import time

d = DesiredCapabilities.CHROME
d['loggingPrefs'] = { 'performance':'ALL' }

#browser options
browser_options = webdriver.ChromeOptions()
browser_options.add_argument('--headless')


#init browser
browser = webdriver.Chrome('/usr/bin/chromedriver', options=browser_options, desired_capabilities=d)
browser.get('https://www.facebook.com/')

#getting fields
fieldLogin = browser.find_element_by_id('email')
fieldPassword = browser.find_element_by_id('pass')

#insertion
fieldLogin.send_keys('gvictor525.gv@gmail.com')
fieldPassword.send_keys('123')

response = fieldLogin.send_keys(Keys.ENTER)

performance_log = browser.get_log('performance')
#print (str(performance_log).strip('[]'))

response = performance_log[5]['message']
response = json.loads(response)

status = response['message']['params']['response']['headers']['status']
print(status)
#value['message']['params']['response']['headers']['status']

ipdb.set_trace()
