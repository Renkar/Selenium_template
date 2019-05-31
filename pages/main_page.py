from time import sleep
from .page import Page, WebDriverException
from elements.blocks.footer import Footer
from allure import step


"""
Class MainPage: In this class, the page blocks are initialized and the main actions take place on the maine page.
"""


class MainPage(Page):

    def __init__(self, driver, base_url):
        self.driver = driver
        self.url = base_url
        self.Footer = Footer(self.driver)

    """
    Step: getting title page
    """
    def step_click_to_small_card_2(self):
        with step('Step: click to 2 small card'):
            self.Footer.terms_and_conditions()
            self.screenshot('Step: click to 2 small card')