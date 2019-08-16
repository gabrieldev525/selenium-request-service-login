import argparse
import requests
import pyquery
from bs4 import BeautifulSoup
import ipdb
from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities



def title(text):
	print('=' * len(text))
	print(text)
	print('=' * len(text))




'''
	Attempt to login to Facebook. Returns True if login sucessful. 
	Returns False if login failed.
'''
def facebook_login(session, email, password):

	# response = session.get('https://m.facebook.com')

	# attempt to login to facebook
	response = session.post('https://m.facebook.com/login.php', data={
		'email': email,
		'pass': password
	}, allow_redirects=False)


	# if c_user cookies is setted, login successful 
	if 'c_user' in response.cookies:
		return True
	else:
		return False




''' 
	attempt to login on instagram
'''
def instagram_login(session, login, password):
	d = DesiredCapabilities.CHROME
	d['loggingPrefs'] = { 'performance':'ALL' }

	#browser options
	browser_options = webdriver.ChromeOptions()
	browser_options.add_argument('--headless')


	#init browser
	browser = webdriver.Chrome('/usr/bin/chromedriver', options=browser_options, desired_capabilities=d)
	browser.get('https://www.facebook.com/')

	try:
	    element = WebDriverWait(browser, 10).until(
	        EC.presence_of_element_located((By.NAME, "username"))
	    )
	finally:
		# values
		loginField = browser.find_element_by_name('username')
		passwordField = browser.find_element_by_name('password')

		# insertion
		loginField.send_keys(login)
		passwordField.send_keys(password)

		loginField.send_keys(Keys.ENTER)

		soup = BeautifulSoup(browser.page_source, 'html.parser')
		print(soup)




session = requests.session()
session.headers.update({
	'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:39.0) Gecko/20100101 Firefox/39.0'
})


# facebook login
title('facebook')

result = facebook_login(session, 'gvictor525.gv@gmail.com', '123')

if result:
	print('login successful')
else:
	print('Login failed')


# instagram login

title('instagram')

# result = instagram_login(session, 'gabrieldev525', 'gabriel525')

