import re
from playwright.sync_api import Page, expect


def test_example(page: Page) -> None:
    page.goto("https://development.didgmuxcg41cu.amplifyapp.com/")
    page.get_by_role("textbox", name="Email ID/Phone").click()
    page.get_by_role("textbox", name="Email ID/Phone").fill("device2@gmail.com")
    page.get_by_role("textbox", name="Password").click()
    page.get_by_role("textbox", name="Password").fill("password123")
    page.get_by_role("button", name="Login Now").click()
    page.get_by_role("link", name="Create Medication").click()
    page.get_by_role("textbox", name="Start typing to get").click()
    page.get_by_role("textbox", name="Start typing to get").fill("t")
    page.get_by_text("Hydralazine 25 Mg Tablet").click()
    page.get_by_role("button", name="Next").click()
    page.get_by_text("Long Term").click()

    # Click + button 2 times
    plus_button = page.get_by_role("button", name="+")
    plus_button.click()
    plus_button.click()

    # Click Next
    page.get_by_role("button", name="Next").click()