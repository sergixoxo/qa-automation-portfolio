import pytest
from playwright.sync_api import Page
from pages.saucedemo_page import SauceDemoPage


@pytest.fixture
def saucedemo_page(page: Page):
    saucedemo = SauceDemoPage(page)
    saucedemo.navigate()

    return saucedemo