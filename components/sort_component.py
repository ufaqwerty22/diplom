import allure
from playwright.sync_api import Page, Locator

from components.base_component import BaseComponent


class SortComponent(BaseComponent):
    def __init__(self, page: Page, wrapper: Locator):
        super().__init__(page, wrapper)

    def click_sort_by_text(self, text: str):
        with allure.step(f'В сортировке нажать на {text}'):
            self.wrapper.locator('div.catalog-sort__current').click()
            self.wrapper.locator(f'//li/a[contains(text(), "{text}")]').click()

    def click_reset_sort_button(self):
        self.wrapper.locator('a.catalog-filter__reset').click()

    def compare_prices_from_lo_to_high(self, max_item = 60):
        count = 0
        for i in range(max_item - 1):
            current_price = self.wrapper.locator(
                f'(//div[contains(@class, "current-price")])[{i + 1}]').inner_text()
            next_price = self.wrapper.locator(
                f'(//div[contains(@class, "current-price")])[{i + 2}]').inner_text()
            current_price_value = int(''.join(filter(str.isdigit, current_price)))
            next_price_value = int(''.join(filter(str.isdigit, next_price)))

            if current_price_value <= next_price_value:
                count += 1
        return count
