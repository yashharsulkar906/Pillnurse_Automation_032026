from pages.base_page import BasePage

class LoginPage(BasePage):
    USERNAME = "#username"
    PASSWORD = "#password"
    LOGIN_BUTTON = "#loginBtn"

    def login(self, username, password):
        self.wait_for_element(self.USERNAME)
        self.fill(self.USERNAME, username)
        self.wait_for_element(self.PASSWORD)
        self.fill(self.PASSWORD, password)
        self.wait_for_element(self.LOGIN_BUTTON)
        self.click(self.LOGIN_BUTTON)