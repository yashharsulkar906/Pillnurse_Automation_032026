import re
from playwright.sync_api import Page, expect


def test_example(page: Page) -> None:
    page.goto("https://development.didgmuxcg41cu.amplifyapp.com/")
    page.get_by_role("textbox", name="Email ID/Phone").click()
    page.get_by_role("textbox", name="Email ID/Phone").fill("device2@gmail.com")
    page.get_by_role("textbox", name="Password").click()
    page.get_by_role("textbox", name="Password").fill("password123")
    page.get_by_role("button", name="Login Now").click()
   