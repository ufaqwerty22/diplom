import allure
from playwright.sync_api import Page, Locator

from components.base_component import BaseComponent


class AddedToCartComponent(BaseComponent):
    def __init__(self, page: Page, wrapper: Locator):
        super().__init__(page, wrapper)

    def click_go_to_cart(self):
        with allure.step('Нажать на кнопку "Перейти в корзину"'):
            self.wrapper.locator('//a[contains(text(), "Перейти в корзину") and contains(@class, "go-to-cart")]').click()