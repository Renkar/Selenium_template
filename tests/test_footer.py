from allure import feature, epic
from elements.locators.locators_header_footer import LOGO, SOCIAL_LINK_FACEBOOK, SOCIAL_LINK_INSTAGRAM, \
    SOCIAL_LINK_TELEGRAM, SOCIAL_LINK_TWITTER, FOOTER_NAV_LINK
import pytest

footer_elements = [LOGO, SOCIAL_LINK_FACEBOOK, SOCIAL_LINK_INSTAGRAM, SOCIAL_LINK_TELEGRAM, \
                   SOCIAL_LINK_TWITTER, FOOTER_NAV_LINK]


@epic("Some_name")
@feature("Footer")
@pytest.mark.parametrize('footer_elements', footer_elements)
def test_check_logo_in_footer(app, footer_elements):
    app.MainPage.scroll_down()
    app.MainPage.step_elements_in_footer_visible(footer_elements)


@epic("Some_name")
@feature("Footer")
def test_terms_and_condition(app):
    app.MainPage.scroll_down()
    app.MainPage.step_click_on_terms_and_condition()

    app.MainPage.step_click_logo()


@epic("Some_name")
@feature("Footer")
def test_privacy_policy_name(app):
    app.MainPage.scroll_down()
    app.MainPage.step_click_on_privacy_policy()
    app.MainPage.step_click_logo()
