from playwright.sync_api import sync_playwright
from playwright.sync_api import expect


with sync_playwright() as p:
    browser =p.chromium.launch(headless=False)
    page=browser.new_page()
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    page.locator("input[name='username']").fill("Admin")
    page.locator("input[name='password']").fill("admin1234")
    #tagname[attribute='value']
    page.locator("button[type='submit']").click()
    #screenshots
    screenshot = page.screenshot(path="screenshot.png")
    print("Screenshot taken and saved as screenshot.png")
    #assertions
    page.have_title("OrangeHRM")
    expect(page.locator)("h6").to_have_text("Dashboard")
    #dropdown
    page.select_option("select#dropdown", "India")
    #handling alerts
    page.on("dialog", lambda dialog: dialog.accept())
    browser.close()
   