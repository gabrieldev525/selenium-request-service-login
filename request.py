import requests

r = requests.post('https://www.facebook.com/login/device-based/regular/login/?login_attempt=1&amp;lwv=110', data={'email':'gvictor525.gv@gmail.com', 'password':'123'})
return_code = r.status_code

print(return_code)