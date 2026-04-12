from playwright.sync_api import Page, Locator

from components.base_component import BaseComponent


class CardMainColumnComponent(BaseComponent):
    def __init__(self, page: Page, wrapper: Locator):
        super().__init__(page, wrapper)

    def get_photo_locator(self):
        return self.wrapper.locator('div.card-photo-slider__main')