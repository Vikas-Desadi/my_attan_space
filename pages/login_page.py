from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    username_txt = (By.ID, "username")
    password_txt = (By.ID, "password")
    login_btn = (By.XPATH, "//input[@id='submit']")
    name_txt = (By.XPATH, "//div[@class='usernameContainer left']//following-sibling::p")

    def login(self, username, password):
        self.send_text(self.username_txt, username)
        self.send_text(self.password_txt, password)
        self.click_login()

    def get_my_name_text(self):
        self.get_text(self.name_txt)
