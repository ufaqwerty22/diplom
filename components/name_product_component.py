from playwright.sync_api import Page, Locator

from components.base_component import BaseComponent


class NameProductComponent(BaseComponent):
    def __init__(self, page: Page, wrapper: Locator):
        super().__init__(page, wrapper)