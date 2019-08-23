from allure_commons.types import AttachmentType
from allure import attach

def screenshot(title: str,driver):
    attach(driver.get_screenshot_as_png(),
