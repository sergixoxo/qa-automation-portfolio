
from playwright.sync_api import Page, expect


def test_homepage_loads_successfully(page: Page):
    response = page.goto("https://playwright.dev/")

    assert response is not None
    assert response.status == 200


def test_homepage_has_expected_title(page: Page):
    page.goto("https://playwright.dev/")

    expect(page).to_have_title(
        "Fast and reliable end-to-end testing for modern web apps | Playwright"
    )


def test_homepage_has_visible_heading(page: Page):
    page.goto("https://playwright.dev/")

    expect(
        page.get_by_role("heading", level=1)
    ).to_be_visible()
