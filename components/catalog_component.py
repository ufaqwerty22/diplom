import allure
from playwright.sync_api import Page, Locator

from components.base_component import BaseComponent


class CatalogComponent(BaseComponent):
    def __init__(self, page: Page, wrapper: Locator):
        super().__init__(page, wrapper)

    def click_product_by_name(self, name: str):
        with allure.step(f'Нажать на товар {name}'):
            self.wrapper.locator(f'//a[contains(text(), "{name}")]').click()

    def get_product_by_name(self, name: str):
        self.wrapper.locator(f'//*[contains(text(), "{name}")]/ancestor::div[@data-mh="catalog-item-col"]')

    def add_product_in_cart_by_name(self, name: str):
        with allure.step(f'Добавить товар {name} в корзину'):
            self.wrapper.locator(
            f'(//a[contains(text(), "{name}")]/following-sibling::div//a[contains(text(), "В корзину")])[2]').click()

    def count_products_by_word(self, word: str, max_items = 60):
        count = 0
        for number in range(max_items):
            title = self.wrapper.locator(
            f'(//div[contains(@class, "col-lg-3 col-md-4")])[{number + 1}]').inner_text()
            if word in title.lower():
                count += 1
        return count