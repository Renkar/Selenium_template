from elements.locators.locators_header_footer import FOOTER, FOOTER_NAV_LINK

"""
Class Footer:  describe block footer on page
"""


class Footer:

    def __init__(self, driver):
        self.driver = driver

    """
    @property: returned  footer block
    """

    @property
    def get_footer(self):
        return self.driver.find_element_by_class_name(FOOTER)

    """
    @property: returned terms and condition element
    """

    @property
    def terms_and_conditions(self):
        elements = self.driver.find_elements_by_class_name(FOOTER_NAV_LINK)
        return elements[0]

    """
    @property: returned  privacy policy element
    """

    @property
    def privacy_policy(self):
        elements = self.driver.find_elements_by_class_name(FOOTER_NAV_LINK)
        return elements[1]
