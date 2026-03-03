from pages.login_page import LoginPage

def test_valid_login(page):
    page.goto("https://development.didgmuxcg41cu.amplifyapp.com/")
    
    login_page = LoginPage(page)
    login_page.login("device2@gmail.com", "password123")

    # Example assertion
    page.wait_for_timeout(3000)
    assert "dashboard" in page.url.lower()

