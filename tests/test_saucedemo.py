from playwright.sync_api import Page, expect
from pages.saucedemo_page import SauceDemoPage


def test_successful_login(saucedemo_page: SauceDemoPage, page: Page):
    saucedemo_page.login("standard_user", "secret_sauce")

    expect(page.get_by_text("Products", exact=True)).to_be_visible()