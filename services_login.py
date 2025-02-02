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


# browser configs
d = DesiredCapabilities.CHROME
d['loggingPrefs'] = { 'performance':'ALL' }

#browser options
browser_options = webdriver.ChromeOptions()
browser_options.add_argument("--headless")


''' 
	autentication

	Facebook - ok
	Instagram - ok
	Twitter - ok
	Github - ok
	Bitbucket - ok
	Office 365 - ok
	Linkedin - ok
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

	driver.quit()


''' 
	attempt to login on instagram
	return True if login has been success
	and return False if login failed
'''
def instagram_login(login, password):
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

	driver.quit()




''' 
	attempt to login on twitter
	return True if login has been success
	and return False if login failed
'''
def twitter_login(login, password):
	#init browser
	driver = webdriver.Chrome('/usr/bin/chromedriver', options=browser_options, desired_capabilities=d)
	driver.get('https://twitter.com/login/')

	#getting fields
	user = driver.find_element_by_class_name("js-username-field")
	user.send_keys(login)
	
	pswd = driver.find_element_by_class_name("js-password-field")
	pswd.send_keys(password)

	user.send_keys(Keys.ENTER)

	print('wait...')
	time.sleep(2)

	if 'error' in driver.current_url:
		driver.quit()
		return False
	else:
		driver.quit()
		return True


''' 
	attempt to login on Github
	return True if login has been success
	and return False if login failed
'''
def github_login(login, password):
	#init browser
	driver = webdriver.Chrome('/usr/bin/chromedriver', options=browser_options, desired_capabilities=d)
	driver.get('https://github.com/login/')

	# getting fields
	driver.find_element_by_name('login').send_keys(login)
	driver.find_element_by_name('password').send_keys(password)
	driver.find_element_by_name('login').send_keys(Keys.ENTER)

	print('wait...')
	time.sleep(2)

	if driver.find_elements_by_css_selector('#js-flash-container .flash-error .container'):
		return False
	else:
		return True


''' 
	attempt to login on Bitbucket
	return True if login has been success
	and return False if login failed
'''#js-flash-container .flash-error .container
def bitbucket_login(login, password):
	#init browser
	driver = webdriver.Chrome('/usr/bin/chromedriver', options=browser_options, desired_capabilities=d)
	driver.get('https://bitbucket.org/account/signin/')

	# getting fields
	user = driver.find_element_by_id('username')
	user.send_keys(login)
	user.send_keys(Keys.ENTER) #continue

	time.sleep(1)

	pswd = driver.find_element_by_id('password')
	pswd.send_keys(password)

	pswd.send_keys(Keys.ENTER) #login

	print('wait...')
	time.sleep(4)

	if driver.find_elements_by_css_selector('#login-error span'):
		return False
	else:
		return True
	
''' 
	attempt to login on Office 365
	return True if login has been success
	and return False if login failed
'''#js-flash-container .flash-error .container
def office365_login(login, password):
	#init browser
	driver = webdriver.Chrome('/usr/bin/chromedriver', options=browser_options, desired_capabilities=d)
	driver.get('https://www.office.com/login?es=Click&ru=%2F%3Fomkt%3Dpt-br')

	#getting fields
	user = driver.find_element_by_name('loginfmt')
	user.send_keys(login)
	user.send_keys(Keys.ENTER) #continue

	time.sleep(2)

	if driver.find_elements_by_css_selector('#usernameError'):
		return False
	else:
		pswd = driver.find_element_by_name('passwd')
		pswd.send_keys(password)

		pswd.send_keys(Keys.ENTER) #login

	print('wait...')
	time.sleep(4)

	if driver.find_elements_by_css_selector('#login-error span') or driver.find_elements_by_css_selector('#error_Info'):
		return False
	else:
		return True

''' 
	attempt to login on Office 365
	return True if login has been success
	and return False if login failed
'''#js-flash-container .flash-error .container
def linkedin_login(login, password):
	#init browser
	driver = webdriver.Chrome('/usr/bin/chromedriver', options=browser_options, desired_capabilities=d)
	driver.get('https://www.linkedin.com/uas/login?_l=pt')

	#getting fields
	user = driver.find_element_by_id('username')
	user.send_keys(login)

	pswd = driver.find_element_by_id('password')
	pswd.send_keys(password)

	pswd.send_keys(Keys.ENTER) #login

	print('wait...')
	time.sleep(2)

	if driver.find_elements_by_css_selector(".form__input--error"):
		return False
	else:
		return True

#======================#
#======= testing ======#
#======================#





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












def resultLogin(result):
	if result:
		print('login successful')
	else:
		print('Login failed')




session = requests.session()
session.headers.update({
	'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:39.0) Gecko/20100101 Firefox/39.0'
})


# facebook login
title('facebook')

result = facebook_login(session, 'gvictor525.gv@gmail.com', 'gabriel123')
resultLogin(result)

# instagram login

title('instagram')

result = instagram_login('gvictor525.gv@gmail.com', 'gabriel123')
resultLogin(result)

# twitter login
title('twitter')

result = twitter_login('gvictor', 'gabriel')
resultLogin(result)

#github login
title('github')
result = github_login('gvictor525.gv@gmail.com', '123')
resultLogin(result)

#Bitbucket
title('bitbucket')
result = bitbucket_login('gvictor525.gv@gmail.com', '123')
resultLogin(result)

#Office 365
title('office 365')
result = office365_login('teste', '123')
resultLogin(result)

#Linkedin
title('Linkedin')
result = linkedin_login('gvictor525.gv@gmail.com', '123')
resultLogin(result)
