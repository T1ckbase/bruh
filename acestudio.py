import requests
from datetime import datetime, timezone, timedelta
import os

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'channel': 'web',
    'device': 'web',
    'platform': 'web',
    'Version': 'web'
}

url = 'https://as-api.tdacestudio.com/api/as/web/auth/code?phone=886-0966513808'

response = requests.get(url, headers=headers)
if response.status_code == requests.codes.ok:
    j = response.json()
    print(j)

with open('acestudio.log', 'a', encoding='utf-8') as f:
    t = datetime.now(timezone(timedelta(hours=+8))).strftime('%Y-%m-%d %H:%M:%S')
    f.write('[' + t + '] ' + response.text + '\n')