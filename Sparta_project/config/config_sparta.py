from playwright.sync_api import sync_playwright, Page, BrowserContext
import pytest


@pytest.fixture
def get_playwright():
    with sync_playwright() as playwright:
        yield playwright



@pytest.fixture
def browser(get_playwright):
    browser = get_playwright.firefox.launch(headless=False)
    yield browser
    browser.close()


@pytest.fixture
def browser_context(browser):
    context = browser.new_context()
    yield context
    context.close()


@pytest.fixture
def page(browser_context: BrowserContext) -> Page:
    page = browser_context.new_page()
    yield page
    page.close()