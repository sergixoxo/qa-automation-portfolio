from playwright.sync_api import expect
from pages.saucedemo_page import SauceDemoPage


def test_login_with_invalid_credentials(saucedemo_page: SauceDemoPage):
    saucedemo_page.login("usuario_incorrecto", "password_incorrecta")

    expect(saucedemo_page.error_message).to_be_visible()
    expect(saucedemo_page.error_message).to_contain_text(
        "Username and password do not match"
    )


def test_login_with_empty_username(saucedemo_page: SauceDemoPage):
    saucedemo_page.login("", "secret_sauce")

    expect(saucedemo_page.error_message).to_be_visible()
    expect(saucedemo_page.error_message).to_contain_text(
        "Username is required"
    )


def test_login_with_empty_password(saucedemo_page: SauceDemoPage):
    saucedemo_page.login("standard_user", "")

    expect(saucedemo_page.error_message).to_be_visible()
    expect(saucedemo_page.error_message).to_contain_text(
        "Password is required"
    )


def test_login_with_locked_out_user(saucedemo_page: SauceDemoPage):
    saucedemo_page.login("locked_out_user", "secret_sauce")

    expect(saucedemo_page.error_message).to_be_visible()
    expect(saucedemo_page.error_message).to_contain_text(
        "Sorry, this user has been locked out"
    )