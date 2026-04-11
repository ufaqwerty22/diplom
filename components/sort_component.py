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