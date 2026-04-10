from playwright.sync_api import Page, Locator

from components.base_component import BaseComponent


class CardAsideColumnComponent(BaseComponent):
    def __init__(self, page: Page, wrapper: Locator):
        super().__init__(page, wrapper)

    def get_price_locator(self):
        self.wrapper.locator('div.card-price__current')

    