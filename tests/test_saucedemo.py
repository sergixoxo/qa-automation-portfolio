from playwright.sync_api import Page, expect
import pytest
from pages.saucedemo_page import SauceDemoPage


def test_successful_login(saucedemo_page: SauceDemoPage, page: Page):
    saucedemo_page.login("standard_user", "secret_sauce")

    expect(page.get_by_text("Products", exact=True)).to_be_visible()

@pytest.mark.xfail(reason="BUG-001: problem_user displays the same image for all products")

def test_problem_user_product_images(saucedemo_page: SauceDemoPage, page: Page):
    saucedemo_page.login("problem_user", "secret_sauce")

    expect(saucedemo_page.products_title).to_be_visible()

    images = saucedemo_page.product_images

    assert images.count() == 6

    image_sources = images.evaluate_all(
    "(images) => images.map((image) => image.getAttribute('src'))"
)

    assert len(set(image_sources)) == 6

@pytest.mark.xfail(reason="BUG-002: problem_user cannot remove products from inventory")
def test_problem_user_remove_button(saucedemo_page: SauceDemoPage, page: Page):
    saucedemo_page.login("problem_user", "secret_sauce")

    expect(saucedemo_page.products_title).to_be_visible()

    saucedemo_page.add_backpack_to_cart()

    expect(saucedemo_page.remove_button).to_be_visible()

    saucedemo_page.remove_button.click()

    expect(saucedemo_page.add_to_cart_button).to_be_visible()