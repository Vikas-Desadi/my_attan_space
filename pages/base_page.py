from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# driver = webdriver.Chrome("/home/vikas/PycharmProjects/myspace_attan/drivers/chromedriver")

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def clear_text(self, by_locator):
        self.wait.until(EC.presence_of_element_located(by_locator)).clear()

    def send_text(self, by_locator, value):
        self.wait.until(EC.presence_of_element_located(by_locator)).send_keys(value)

    def click(self, by_locator):
        self.wait.until(EC.presence_of_element_located(by_locator)).click()

    def click_login(self):
        lgn_btn = self.driver.find_element_by_xpath('//input[@id="submit"]')
        self.driver.execute_script("arguments[0].click();", lgn_btn)

    def click_element(self, element):
        self.wait.until(EC.visibility_of(element)).click()

    def wait_for(self, by_locator):
        self.wait.until(EC.visibility_of_element_located(by_locator))

    def get_inner_text(self, by_locator):
        return self.wait.until(EC.visibility_of_element_located(by_locator)).get_attribute("innerText")

    def get_text(self, by_locator):
        return self.wait.until(
            EC.visibility_of_all_elements_located(by_locator)).text

    def wait_for_elements(self, by_locator):
        self.wait.until(EC.visibility_of_all_elements_located(by_locator))