from playwright.sync_api import Page, expect

def test_create_new_patient(page: Page) -> None:
    page.goto("https://development.didgmuxcg41cu.amplifyapp.com/")

    page.get_by_placeholder("Email ID/phone").fill("device2@gmail.com")
    page.get_by_placeholder("password").fill("Password123")

    page.get_by_role("button", name="Login Now").click()

    expect(page).to_have_url(lambda url: "dashboard" in url.lower())