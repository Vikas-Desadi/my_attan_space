import time

import pytest
from selenium import webdriver

import settings
from pages.base_page import BasePage
from pages.home_page import HomePage
from pages.login_page import LoginPage


driver = None


def pytest_addoption(parser):
    parser.addoption("--browser", action='store', default=settings.browser)


@pytest.fixture()
def getBrowser(request):
    _browser = request.config.getoption("--browser")
    return _browser


@pytest.fixture()
def get_driver(request, getBrowser):
    global driver
    if getBrowser == "chrome":
        driver = webdriver.Chrome(settings.chrome_path)
        driver.get(settings.url)
        driver.implicitly_wait(20)
        # request.cls.basePage = BasePage(_driver)
        request.cls.loginPage = LoginPage(driver)
        request.cls.homePage = HomePage(driver)
        # request.cls.driver = _driver
        yield driver
        time.sleep(2)
        # driver.quit()