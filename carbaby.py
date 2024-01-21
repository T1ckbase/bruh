import requests
from datetime import datetime, timezone, timedelta

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'content-type': 'application/x-www-form-urlencoded;charset=UTF-8'
}

data = {
    'action': 'sendCode',
    'phone': '0966513808'
}

url = 'https://www.carbaby.com.tw/wp-admin/admin-ajax.php'

response = requests.post(url, headers=headers, data=data)
if response.status_code == requests.codes.ok:
    print(response.text)

with open('carbaby.log', 'a', encoding='utf-8') as f:
    t = datetime.now(timezone(timedelta(hours=+8))).strftime('%Y-%m-%d %H:%M:%S')
    f.write('[' + t + '] ' + response.text + '\n')