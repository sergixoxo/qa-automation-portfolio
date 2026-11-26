
import pytest
from playwright.sync_api import expect, TimeoutError as PlaywrightTimeoutError
from pages.saucedemo_page import SauceDemoPage


def test_complete_purchase_flow(saucedemo_page: SauceDemoPage):
    # 1. Login
    saucedemo_page.login("standard_user", "secret_sauce")
    expect(saucedemo_page.products_title).to_be_visible()

    # 2. Select product and add it to cart
    expect(saucedemo_page.backpack).to_be_visible()
    expect(saucedemo_page.backpack).to_contain_text("29.99")

    saucedemo_page.add_backpack_to_cart()
    expect(saucedemo_page.remove_button).to_be_visible()

    # 3. Open cart and validate product
    expect(saucedemo_page.shopping_cart_link).to_contain_text("1")
    saucedemo_page.open_cart()

    expect(saucedemo_page.cart_item).to_have_count(1)
    expect(saucedemo_page.cart_item).to_contain_text("Sauce Labs Backpack")
    expect(saucedemo_page.cart_item).to_contain_text("29.99")
    expect(saucedemo_page.cart_item_quantity).to_have_text("1")

    # 4. Start checkout
    saucedemo_page.start_checkout()

    # 5. Complete customer information
    saucedemo_page.fill_checkout_information(
        first_name="Sergio",
        last_name="Sanabria",
        postal_code="110111"
    )

    # 6. Validate checkout overview
    expect(saucedemo_page.cart_item).to_have_count(1)
    expect(saucedemo_page.cart_item).to_contain_text("Sauce Labs Backpack")
    expect(saucedemo_page.cart_item).to_contain_text("29.99")
    expect(saucedemo_page.cart_item_quantity).to_have_text("1")

    expect(saucedemo_page.page.locator(".summary_subtotal_label")).to_have_text(
        "Item total: $29.99"
    )

    expect(saucedemo_page.page.locator(".summary_tax_label")).to_be_visible()
    expect(saucedemo_page.page.locator(".summary_total_label")).to_be_visible()

    # 7. Finish purchase
    saucedemo_page.finish_purchase()

    # 8. Validate purchase confirmation
    expect(saucedemo_page.complete_header).to_have_text("Thank you for your order!")
    expect(saucedemo_page.page.locator(".complete-text")).to_be_visible()


@pytest.mark.xfail(
    reason="BUG-003: Checkout allowed with an empty cart (proposed business rule)",
    strict=True,
    raises=pytest.fail.Exception
)

def test_checkout_with_empty_cart(saucedemo_page: SauceDemoPage):
    # 1. Login
    saucedemo_page.login("standard_user", "secret_sauce")
    expect(saucedemo_page.products_title).to_be_visible()

    # 2. Open and validate empty cart
    saucedemo_page.open_cart()
    expect(saucedemo_page.cart_item).to_have_count(0)

    # 3. Start checkout
    saucedemo_page.start_checkout()

    # 4. Complete customer information
    saucedemo_page.fill_checkout_information(
        first_name="Test",
        last_name="Customer",
        postal_code="110111"
    )

    # 5. Verify that the checkout overview is empty
    expect(saucedemo_page.cart_item).to_have_count(0)

    # 6. Attempt to finish purchase
    saucedemo_page.finish_purchase()

    # 7. Check whether an invalid purchase is confirmed
    try:
        saucedemo_page.complete_header.wait_for(
        state="visible",
        timeout=5000
    )
    except PlaywrightTimeoutError:
        pass
    else:
        pytest.fail("BUG-003: Empty cart purchase was confirmed")