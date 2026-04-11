import allure
from playwright.sync_api import Page, Locator

from components.base_component import BaseComponent
from controls.button_control import ButtonControl


class ProductInCartComponent(BaseComponent):
    def __init__(self, page: Page, wrapper: Locator):
        super().__init__(page, wrapper)
        self.__delete_product_from_cart_btn = ButtonControl(self.page, self.wrapper.locator(
            'div.basket-item-block-actions'))

    def click_delete_product_btn(self):
        with allure.step('Удалить товар из коризны'):
            self.__delete_product_from_cart_btn.click_anyway()