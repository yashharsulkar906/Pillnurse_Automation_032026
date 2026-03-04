import re
from playwright.sync_api import Page, expect


def test_example(page: Page) -> None:
    page.goto("https://staging.d2kcjp2bs55j6j.amplifyapp.com/")
    page.get_by_role("button", name="Patient List").click()
    page.get_by_role("button", name="Sync and use this patient").nth(1).click()
    page.get_by_role("button", name="📊 Live Dashboard").click()
    page.get_by_role("spinbutton").first.click()
    page.get_by_role("spinbutton").first.fill("01")
    page.get_by_role("spinbutton").nth(1).click()
    page.get_by_role("spinbutton").nth(1).fill("")
    page.get_by_role("spinbutton").nth(1).click()
    page.get_by_role("spinbutton").nth(1).click()
    page.get_by_role("spinbutton").nth(1).click()
    page.get_by_role("spinbutton").nth(1).fill("05")
    page.get_by_role("combobox").nth(1).select_option("Seconds")
    page.get_by_role("textbox").click()
    page.get_by_role("textbox").click()
    page.get_by_role("textbox").click()
    page.get_by_role("button", name="Launch Simulation Loop").click()
    page.get_by_role("button", name="Stop Simulation").click()
    page.get_by_role("button", name="Patient List").click()
    page.get_by_role("button", name="Continue with this patient").click()
    page.get_by_role("button", name="📋 Clinical Records").click()
