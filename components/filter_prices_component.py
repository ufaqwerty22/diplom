import allure
from playwright.sync_api import Page, Locator

from components.base_component import BaseComponent


class FilterPricesComponent(BaseComponent):
    def __init__(self, page: Page, wrapper: Locator):
        super().__init__(page, wrapper)

    def hover_and_click_by_text(self, text: str):
        with allure.step(f'В фильтре навести курсор на {text} и кликнуть'):
            self.wrapper.get_by_text(text).hover()
            self.wrapper.get_by_text(text).click()

    def enter_min_price(self, min_price: str):
        with allure.step(f'Ввести минимальную цену в фильтре {min_price}'):
            self.wrapper.locator('//input[contains(@class, "field-min-price")]').fill(min_price)

    def enter_max_price(self, max_price: str):
        with allure.step(f'Ввести максимальную цену в фильтре {max_price}'):
            self.wrapper.locator('//input[contains(@class, "field-max-price")]').fill(max_price)

    def click_submit_button(self):
        with allure.step('Нажать на кнопку "Применить" в фильтре цен'):
            self.wrapper.locator('//button[@type="submit" and text()="Применить"]').click()

    def compare_prices_of_products(self, min_price: int, max_price: int, max_items = 60):
        count = 0
        for i in range(max_items):
            price = self.wrapper.locator(
                f'(//div[contains(@class, "current-price")])[{i + 1}]').inner_text()
            price_value = int(''.join(filter(str.isdigit, price)))
            if min_price <= price_value <= max_price:
                count += 1
        return count