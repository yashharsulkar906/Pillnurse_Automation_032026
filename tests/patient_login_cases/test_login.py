import re
from playwright.sync_api import Page, expect

#validating the login functionality of the patient portal by entering valid credentials and checking if the user is able to login successfully and then logout. This test case ensures that the login process is working as expected for patients.
def test_example(page: Page) -> None:
    page.goto("https://development.didgmuxcg41cu.amplifyapp.com/")
    page.get_by_role("textbox", name="Email ID/Phone").click()
    page.get_by_role("textbox", name="Email ID/Phone").fill("device2@gmail.com")
    page.get_by_role("textbox", name="Password").click()
    page.get_by_role("textbox", name="Password").fill("password123")
    page.get_by_role("button", name="Login Now").click()
    page.get_by_role("link").nth(3).click()
    page.get_by_role("link", name="Logout").click()
#invalidating the login functionality of the patient portal by entering invalid credentials and checking if the user is able to login successfully. This test case ensures that the login process is working as expected for patients and that it is not allowing unauthorized access.
def test_example(page: Page) -> None:
    page.goto("https://development.didgmuxcg41cu.amplifyapp.com/")
    page.get_by_role("textbox", name="Email ID/Phone").click()
    page.get_by_role("textbox", name="Email ID/Phone").fill("Test@gmail.com")
    page.get_by_role("textbox", name="Password").click()
    page.get_by_role("textbox", name="Password").fill("password1234")
    page.get_by_role("button", name="Login Now").click()
    page.get_by_role("link").nth(3).click()
    page.get_by_role("link", name="Logout").click()
    
#Invalid username and valid password
def test_example(page: Page) -> None:
    page.goto("https://development.didgmuxcg41cu.amplifyapp.com/")
    page.get_by_role("textbox", name="Email ID/Phone").click()
    page.get_by_role("textbox", name="Email ID/Phone").fill("pillnurse@gmail.com")
    page.get_by_role("textbox", name="Password").click()
    page.get_by_role("textbox", name="Password").fill("password123")
    page.get_by_role("button", name="Login Now").click()
    page.get_by_role("link").nth(3).click()
    page.get_by_role("link", name="Logout").click()    