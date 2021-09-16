from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import settings
from tests.base_test import BaseTest

# driver = webdriver.Chrome(executable_path="/home/vikas/PycharmProjects/myspace_attan/drivers/chromedriver")
#
# driver.get("https://myspace.innominds.com/user/login")
# username = driver.find_element_by_id("username").send_keys('pdesadi')
# password = driver.find_element_by_id('password').send_keys('Newjob@123')
# sbt_btn = driver.find_element_by_xpath('//input[@id="submit"]')
# driver.execute_script("arguments[0].click();", sbt_btn)
# WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='submit'']"))).click()
# element = driver.find_element_by_class_name('div[class*="loginsubmit loginSubmitCss"]')
# driver.execute_script("arguments[0].click();", element)


class TestLogin(BaseTest):

    def test_valid_login(self):
        self.loginPage.login(settings.username, settings.password)
        # self.homePage.wait_for_my_name()
        assert "Praneeth Vikas Desadi" in self.loginPage.get_my_name_text()