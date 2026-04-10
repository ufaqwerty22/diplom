from playwright.sync_api import Page, Locator

from components.base_component import BaseComponent


class FilterPricesComponent(BaseComponent):
    def __init__(self, page: Page, wrapper: Locator):
        super().__init__(page, wrapper)

    def hover_and_click_by_text(self, text: str):
        self.wrapper.get_by_text(text).hover()
        self.wrapper.get_by_text(text).click()

    def enter_min_price(self, min_price: str):
        self.wrapper.locator('//input[contains(@class, "field-min-price")]').fill(min_price)

    def enter_max_price(self, max_price: str):
        self.wrapper.locator('//input[contains(@class, "field-max-price")]').fill(max_price)

    def click_submit_button(self):
        self.wrapper.locator('//button[@type="submit" and text()="Применить"]').click()
