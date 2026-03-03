from pages.base_page import BasePage

class LoginPage(BasePage):

    USERNAME = "#username"
    PASSWORD = "#password"
    LOGIN_BUTTON = "#loginBtn"

    def login(self, username, password):
        self.fill(self.USERNAME, username)
        self.fill(self.PASSWORD, password)
        self.click(self.LOGIN_BUTTON)