import argparse
import requests
import pyquery
from bs4 import BeautifulSoup
import ipdb
from selenium import webdriver
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


import urllib, urllib2, cookielib


def title(text):
	print('=' * len(text))
	print(text)
	print('=' * len(text))


''' 
	autentication

	Facebook - ok
	instagram - ok

'''


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

	# print(response.cookies)

	# if c_user cookies is setted, login successful 
	if 'c_user' in response.cookies:
		return True
	else:
		return False





def gmail_login(session, login, password):
	# form_data={'Email': login, 'Passwd': password}
	# post = "https://accounts.google.com/signin/challenge/sl/password"

	# with requests.Session() as s:
	# 	soup = BeautifulSoup(s.get("https://mail.google.com").text, features="lxml")
	# 	for inp in soup.select("#gaia_loginform input[name]"):
	# 		if inp["name"] not in form_data:
	# 			form_data[inp["name"]] = inp["value"]
	# 	s.post(post, form_data)

	# 	html = s.get("https://mail.google.com/mail/u/0/#inbox").content

	# 	return 'GMAIL_LOGIN' in html

	response = session.post('https://accounts.google.com/signin/challenge/sl/password', data={
		'Email': login, 'Passwd': password
	}, allow_redirects=False)

	print(response.cookies)

	# if c_user cookies is setted, login successful 
	if 'GMAIL_LOGIN' in response.cookies:
		return True
	else:
		return False






''' 
	attempt to login on instagram
'''
def instagram_login(login, password):
	d = DesiredCapabilities.CHROME
	d['loggingPrefs'] = { 'performance':'ALL' }

	#browser options
	browser_options = webdriver.ChromeOptions()
	browser_options.add_argument('--headless')


	#init browser
	driver = webdriver.Chrome('/usr/bin/chromedriver', options=browser_options, desired_capabilities=d)
	driver.get('https://www.instagram.com/accounts/login/')

	#getting fields
	driver.find_element_by_name('username').send_keys(login)
	driver.find_element_by_name('password').send_keys(password)
	driver.find_element_by_name('username').send_keys(Keys.ENTER)

	print('wait...')
	time.sleep(2)

	if driver.find_elements_by_css_selector('#slfErrorAlert'):
		return False
	else:
		return True









session = requests.session()
session.headers.update({
	'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:39.0) Gecko/20100101 Firefox/39.0'
})


# facebook login
title('facebook')

result = facebook_login(session, 'gvictor525.gv@gmail.com', 'gabriel525')

if result:
	print('login successful')
else:
	print('Login failed')


# instagram login

title('instagram')

result = instagram_login('gvictor525.gv@gmail.com', 'gabriel52')
if result:
	print('login successful')
else:
	print('Login failed')

title('gmail')

result = gmail_login(session, 'gvictor525.gv@gmail.com', 'gabriel52')
print(result)