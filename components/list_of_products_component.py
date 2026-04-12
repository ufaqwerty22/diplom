import allure
from playwright.sync_api import Page, Locator

from components.base_component import BaseComponent


class ListOfProductsComponent(BaseComponent):
    def __init__(self, page: Page, wrapper: Locator):
        super().__init__(page, wrapper)

    def get_locator_by_name_product(self, name: str):
        return self.wrapper.locator(f'//span[contains(text(), "{name}")]')

    def get_name_product(self, name: str):
        return self.wrapper.locator(f'//span[contains(text(), "{name}")]').inner_text()

    def get_count_of_products(self):
        return self.wrapper.locator('//tr[contains(@class, "basket-items-list-item-container")]').count()

    def get_locator_count_of_product_by_name(self, name: str):
        return self.wrapper.locator(
            f"//span[contains(text(), '{name}')]"
            f"/ancestor::div[@class='basket-items-list']//input[@class='basket-item-amount-filed']")

    def enter_count_of_product(self, count: str):
        with allure.step(f'Ввести количество товара: {count}'):
            self.wrapper.locator('input.basket-item-amount-filed').fill(count)