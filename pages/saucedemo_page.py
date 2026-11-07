
from playwright.sync_api import Page


class SauceDemoPage:

    def __init__(self, page: Page):
        self.page = page

        # Login
        self.username_input = page.get_by_placeholder("Username")
        self.password_input = page.get_by_placeholder("Password")
        self.login_button = page.get_by_role("button", name="Login")
        self.error_message = page.get_by_role("alert")

        # Inventory
        self.products_title = page.get_by_text("Products", exact=True)
        self.backpack = page.locator(".inventory_item").filter(
            has_text="Sauce Labs Backpack"
        )
        self.add_to_cart_button = self.backpack.get_by_role(
            "button", name="Add to cart"
        )

        # Shopping cart
        self.shopping_cart_link = page.locator(".shopping_cart_link")
        self.cart_item = page.locator(".cart_item")
        self.checkout_button = page.get_by_role("button", name="Checkout")

        # Checkout information
        self.first_name_input = page.get_by_placeholder("First Name")
        self.last_name_input = page.get_by_placeholder("Last Name")
        self.postal_code_input = page.get_by_placeholder("Zip/Postal Code")
        self.continue_button = page.get_by_role("button", name="Continue")

        # Checkout overview and confirmation
        self.finish_button = page.get_by_role("button", name="Finish")
        self.complete_header = page.locator(".complete-header")

    def navigate(self):
        self.page.goto("https://www.saucedemo.com/")

    def login(self, username: str, password: str):
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()

    def add_backpack_to_cart(self):
        self.add_to_cart_button.click()

    def open_cart(self):
        self.shopping_cart_link.click()

    def start_checkout(self):
        self.checkout_button.click()

    def fill_checkout_information(
        self, first_name: str, last_name: str, postal_code: str
    ):
        self.first_name_input.fill(first_name)
        self.last_name_input.fill(last_name)
        self.postal_code_input.fill(postal_code)
        self.continue_button.click()

    def finish_purchase(self):
        self.finish_button.click()
