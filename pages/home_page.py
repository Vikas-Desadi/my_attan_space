import time
from datetime import timedelta, date, datetime

from selenium.common.exceptions import StaleElementReferenceException, \
    NoSuchElementException
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    name_txt = (
    By.XPATH, "//div[@class='usernameContainer left']//following-sibling::p")
    timesheet_lnk = (By.XPATH, "//a[contains(text(),'Time Sheets')]")
    day_no_txt = (By.XPATH, "//table[@class='fc-border-separate']//tbody//tr//div//div")
    weeks_lnks = (By.XPATH, "//table[@class='fc-border-separate']//tbody//tr")
    weekdays_lnks = (By.XPATH, "//table[@class='fc-border-separate']//tbody//tr//div//div//div")
    hours_txt = (By.ID, "hours_0_2")
    description_txt = (By.ID, "notes_0_2")
    save_btn = (By.CSS_SELECTOR, "#sub")
    logout_lnk = (By.XPATH, "//a[@href = '/user/logout']")

    def click_timesheet(self):
        self.click(self.timesheet_lnk)

    def wait_for_my_name(self):
        self.wait_for(self.timesheet_lnk)

    def wait_for_time_sheet_link(self):
        self.wait_for(self.timesheet_lnk)

    def click_specific_date(self):
        today = date.today()
        yesterday = str(today - timedelta(days=1))
        lnks = self.driver.find_elements_by_css_selector(".fc-event.fc-event")
        efforts_status = self.driver.find_elements_by_css_selector(".fc-event-title")
        # print(self.day_no_txt)
        try:
            for ele in lnks:
                # import pdb; pdb.set_trace()
                dte = ele.get_attribute('href').split("=")[-1]
                dte_date = datetime.strptime(dte, '%Y-%m-%d').date()
                # print(dte_date)
                for e in efforts_status:
                    if e.text == "" and dte_date.isoweekday() not in ['6', '7']:
                        print(dte_date)
                        print(e.text)
                        self.click_element(ele)
                        time.sleep(10)
                        break

        except (NoSuchElementException, StaleElementReferenceException):
            pass

    def click_today_date(self):
        today = date.today()
        yesterday = str(today - timedelta(days=1))
        lnks = self.driver.find_elements_by_css_selector(".fc-event.fc-event")
        efforts_status = self.driver.find_elements_by_css_selector(
            ".fc-event-title")
        try:
            for ele in lnks:
                dte = ele.get_attribute('href').split("=")[-1]
                if dte == yesterday:
                    self.click_element(ele)
                    break

        except (NoSuchElementException, StaleElementReferenceException):
            pass

    def add_hours_and_desc(self, hours, desc):
        self.wait_for(self.hours_txt)
        self.clear_text(self.hours_txt)
        self.clear_text(self.description_txt)
        self.send_text(self.hours_txt, hours)
        self.send_text(self.description_txt, desc)
        self.click(self.save_btn)

    def signout(self):
        self.click(self.logout_lnk)

    def close_browser(self):
        self.driver.quit()
