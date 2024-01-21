from playwright.sync_api import sync_playwright, TimeoutError as PlaywrightTimeoutError
from datetime import datetime, timezone, timedelta

state = ''

with sync_playwright() as p:
    browser = p.firefox.launch(headless=True)
    context = browser.new_context()

    page = context.new_page()
    page.goto('https://www.ubereats.com/login-redirect/') 
    page.locator('#PHONE_NUMBER_or_EMAIL_ADDRESS').fill('0966513808')
    page.locator('#forward-button').click()

    try:
        page.locator("#PHONE_SMS_OTP-0").fill('0', timeout=5000)
        print('ok')
        state = 'ok'
    except PlaywrightTimeoutError:
        print('Timeout!')
        state = 'error'

    page.pause()
    browser.close()

with open('ubereats.log', 'a', encoding='utf-8') as f:
    t = datetime.now(timezone(timedelta(hours=+8))).strftime('%Y-%m-%d %H:%M:%S')
    f.write('[' + t + '] ' + state + '\n')