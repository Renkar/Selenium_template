from selenium.webdriver.support.expected_conditions import *
from allure_commons.types import AttachmentType
from allure import attach
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import requests

"""
Class Page : basic page class
"""


class Page(object):

    def __init__(self, driver, base_url):
        self.driver = driver
        self.base_url = base_url
        self.wait = WebDriverWait(driver, 10)

    """
    This function check element is visible
    """

    def is_element_visible(self, locator):
        try:
            self.wait.until(visibility_of_element_located(locator))
            return True
        except WebDriverException:
            return False

    """
    This function make screen shot
    """

    def screenshot(self, title: str):
        attach(self.driver.get_screenshot_as_png(), name=title, attachment_type=AttachmentType.PNG)

    """
    This function scroll down page
    """

    def scroll_down(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    """
    This function switch to last open tab
    """

    def switch_to_last_tab(self):
        self.driver.switch_to.window(self.driver.window_handles[-1])

    """
    This function close tab and switch to first network page 
    """

    def close_tab(self):
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])

    """
    This function waiting element on page
    """

    def wait_element(self, locator):
        WebDriverWait(self.driver, 120).until(EC.presence_of_element_located((By.CLASS_NAME, locator)))

    """
    This function image check url status
    """

    def check_status_code_url(self, url):
        status = requests.get(url)
        assert status.status_code == 200

    """
    This function mouse over to  web element
    """

    def mouse_over_element(self, element):
        hover = ActionChains(self.driver).move_to_element(element).perform()
