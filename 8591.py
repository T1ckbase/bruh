import requests
from datetime import datetime, timezone, timedelta

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'content-type': 'application/x-www-form-urlencoded;charset=UTF-8'
}

params = {
    'module': 'user',
    'action': 'userNewRegCheck',
    'type': 'phoneNum',
    'param': '0966513808'
}

url = 'https://www.8591.com.tw/ajax.php'

response = requests.get(url, headers=headers, params=params)
if response.status_code == requests.codes.ok:
    print(response.text)

with open('8591.log', 'a', encoding='utf-8') as f:
    t = datetime.now(timezone(timedelta(hours=+8))).strftime('%Y-%m-%d %H:%M:%S')
    f.write('[' + t + '] ' + response.text + '\n')