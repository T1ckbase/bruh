from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.firefox.launch(headless=False)
    context = browser.new_context()

    page = context.new_page()
    page.goto('https://www.ubereats.com/login-redirect/') 
    page.locator('#PHONE_NUMBER_or_EMAIL_ADDRESS').fill('0966513808')
    page.locator('#forward-button').click()

    page.pause()