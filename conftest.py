import pytest
from playwright.sync_api import sync_playwright
from dotenv import load_dotenv


@pytest.fixture(scope="function", autouse=False)
def page():
    load_dotenv()
    playwright = sync_playwright().start()
    browser = playwright.chromium.launch(headless=False, args=['--start-maximized'])
    context = browser.new_context(no_viewport=True)
    page = context.new_page()
    yield page
    browser.close()
    playwright.stop()