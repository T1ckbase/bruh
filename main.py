import requests
# import json

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'content-type': 'application/x-www-form-urlencoded;charset=UTF-8'
}

data = {
    'mobileCountry': '886',
    'mobile': '0966513808',
    'birthday': '20040803'
}

url = 'https://group.openpoint.com.tw/auth/service/ajax/login/forget-pwd/send-sms-code'

response = requests.post(url, headers=headers, data=data)
if response.status_code == requests.codes.ok:
    j = response.json()
    print(j)
    if j['codeId'] == '200':
        with open('t.txt', 'r') as f:
            n = int(f.read())

        with open('t.txt', 'w') as f:
            f.write(str(n+1))

with open('log.txt', 'a', encoding='utf-8') as f:
    f.write(response.text + '\n')