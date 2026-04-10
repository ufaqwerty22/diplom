from playwright.sync_api import Page, Locator


class BaseControl:
    def __init__(self, page: Page, wrappper: Locator):
        self.page: Page = page
        self.wrapper: Locator = wrappper

    def click_anyway(self):
        self.wrapper.click(force=True)

    def fill(self, text: str):
        self.wrapper.fill(text)