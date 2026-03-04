from playwright.sync_api import Page, expect


def test_simulation_start_stop(page: Page):

    page.goto("https://staging.d2kcjp2bs55j6j.amplifyapp.com/")

    page.get_by_role("button").nth(5).click()

    page.get_by_role("spinbutton").first.fill("02")
    page.get_by_role("combobox").first.select_option("Minutes")

    page.get_by_role("spinbutton").nth(1).fill("01")
    page.get_by_role("combobox").nth(1).select_option("Seconds")

    page.get_by_role("button", name="Launch Simulation Loop").click()

    # Assert Stop button becomes visible
    stop_button = page.get_by_role("button", name="Stop Simulation")
    expect(stop_button).to_be_visible()

    stop_button.click()

    # Optional: verify launch button appears again
    expect(page.get_by_role("button", name="Launch Simulation Loop")).to_be_visible()