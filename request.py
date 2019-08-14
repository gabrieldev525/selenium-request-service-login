from bs4 import BeautifulSoup
import requests
import ipdb


facebook_headers = {
  'content-type': 'application/json',
  'Host': 'www.facebook.com',
  'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0'
}

response = requests.post('https://www.facebook.com/login/device-based/regular/login/?login_attempt=1&amp;lwv=110', data={'email':'gvictor525.gv@gmail.com', 'pass':'123'}, headers=facebook_headers)
return_code = response.status_code
print(return_code)

soup = BeautifulSoup(response.text, 'html.parser')
print(soup.prettify())

ipdb.set_trace()
