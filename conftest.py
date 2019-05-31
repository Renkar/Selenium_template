from models.application import Application
from allure_commons.types import AttachmentType
from allure import attach
from selenium import webdriver
from config import CHROMEDRIVER, GECKODRIVER
import pytest


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="browser type")
    parser.addoption("--base_url", action="store", default=URL, help="base URL")


@pytest.fixture(scope="session")
def browser_type(request):
    return request.config.getoption("--browser")


@pytest.fixture(scope="session")
def base_url(request):
    return request.config.getoption("--base_url")


@pytest.fixture(scope="module")
def app(request, browser_type, base_url):
    if browser_type == "firefox":
        driver = webdriver.Firefox(GECKODRIVER)
    elif browser_type == "chrome":
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--window-size=1920,1080')
        chrome_options.add_argument('--enable-logging')
        chrome_options.add_argument('--v=1')
        chrome_options.add_argument('--ignore-certificate-errors')
        chrome_options.add_argument('--disable-extensions')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--enable-popup-blocking')
        chrome_options.add_argument('--disable-notifications')
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--use-gl=osmesa')
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument('--disable-infobars')
        driver = webdriver.Chrome(CHROMEDRIVER, options=chrome_options)

    def fin():

        screenshot("END TEST", driver)
        driver.get(base_url)
        driver.quit()

    request.addfinalizer(fin)
    return Application(driver, base_url)


def screenshot(title: str, driver):
    attach(driver.get_screenshot_as_png(),
           name=title, attachment_type=AttachmentType.PNG)
