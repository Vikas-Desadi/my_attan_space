import settings
from tests.base_test import BaseTest


class TestHome(BaseTest):

    def teardown_method(self):
        self.homePage.signout()
        self.homePage.close_browser()

    def test_mysheet(self):
        self.loginPage.login(settings.username, settings.password)
        self.homePage.wait_for_time_sheet_link()
        self.homePage.click_timesheet()
        self.homePage.click_today_date()
        self.homePage.add_hours_and_desc("9", "coding")
